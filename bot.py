#!/usr/bin/env python

__author__ = "RJ45"
__authors__ = ["allansw", "linaccess"]
__copyright__ = "Copyright 2013, Linaccess"
__credits__ = ["allansw", "dragonmaster"]
__license__ = "GPL v3"
__version__ = "1.0"
__maintainer__ = "Linaccess"
__email__ = "allansw@"
__status__ = "Linaccess"

import os
import Queue
import sys
import time
import platform
import re
from os import fork, chdir, setsid, umask
from sys import exit
import datetime

sys.path += ['plugins', 'lib']  # so 'import hook' works without duplication
os.chdir(sys.path[0] or '.')  # do stuff relative to the install directory
logfile = os.path.join('/var/log/RJ45/RJ45.log')
def log_write(log, pre, separator, content):
    '''Writes a log line into the logs

    Opens file 'log' and appends the 'content' preceded by 'pre' and 'separator'
    '''
    with open(log, 'a') as log_file:
        try:
            log_file.write(pre + separator + content)
        except Exception as e:
            print err.LOG_FAILURE + '\n' + str(e)

def get_datetime():
    '''Returns a dictionary containing the date and time

    dt['time'] - contains current time in hh:mm format(24 hrs)
    dt['date'] - contains current date as dd-mm-yyyy format
    '''
    dt = {}

    now = datetime.datetime.now()
    dt['time'] = now.strftime('%H:%M')
    dt['date'] = now.strftime('%d-%m-%Y')

    return dt



if __name__ == "__main__":
  try:
    pid = fork()
    if pid > 0:
      exit(0)
  except OSError, e:
    exit(1)
  
  chdir("/usr/share/RJ45")
  setsid()
  umask(0)
  
  try:
    pid = fork()
    if pid > 0:
      exit(0)
  except OSError, e:
    exit(1)


class Bot(object):
    pass

content = 'Linaccess %s (%s) <http://RJ45.linaccess.com/>' % (__version__, __status__)
log_write(logfile, get_datetime()['time'], '<>', content +'\n')

opsys = platform.platform()
python_imp = platform.python_implementation()
python_ver = platform.python_version()
architecture = ' '.join(platform.architecture())

content = "Operating System: %s, Python " \
        "Version: %s %s, Architecture: %s" \
        "" % (opsys, python_imp, python_ver, architecture)

log_write(logfile, get_datetime()['time'], '<>', content +'\n')

bot = Bot()
bot.vars = {}
bot.start_time = time.time()

content = 'Loading plugins...'
log_write(logfile, get_datetime()['time'], '<>', content +'\n')

# bootstrap the reloader
eval(compile(open(os.path.join('core', 'reload.py'), 'U').read(),
    os.path.join('core', 'reload.py'), 'exec'))
reload(init=True)

config()
if not hasattr(bot, 'config'):
    exit()

content = 'Connecting to IRC...'
log_write(logfile, get_datetime()['time'], '<>', content +'\n')

bot.conns = {}

try:
    for name, conf in bot.config['connections'].iteritems():
        # strip all spaces and capitalization from the connection name
        name = name.replace(" ", "_")
        name = re.sub('[^A-Za-z0-9_]+', '', name)
        content = 'Connecting to server: %s' % conf['server']
        log_write(logfile, get_datetime()['time'], '<>', content +'\n')

        if conf.get('ssl'):
            bot.conns[name] = SSLIRC(name, conf['server'], conf['nick'], conf=conf,
                    port=conf.get('port', 6667), channels=conf['channels'],
                    ignore_certificate_errors=conf.get('ignore_cert', True))
        else:
            bot.conns[name] = IRC(name, conf['server'], conf['nick'], conf=conf,
                    port=conf.get('port', 6667), channels=conf['channels'])
except Exception as e:
    content =  'ERROR: malformed config file', e
    log_write(logfile, get_datetime()['time'], '<>', content +'\n')
    sys.exit()

bot.persist_dir = os.path.abspath('persist')
if not os.path.exists(bot.persist_dir):
    os.mkdir(bot.persist_dir)

content = 'Connection(s) made, starting main loop.'
log_write(logfile, get_datetime()['time'], '<>', content +'\n')


fork = os.fork()
if fork:
  while True:
    reload()  # these functions only do things
    config()  # if changes have occured

    for conn in bot.conns.itervalues():
        try:
            out = conn.out.get_nowait()
            main(conn, out)
        except Queue.Empty:
            pass
    while all(conn.out.empty() for conn in bot.conns.itervalues()):
        time.sleep(.1)
