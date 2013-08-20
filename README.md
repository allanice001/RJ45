RJ45
====

Configurable IRC Bot

## About

RJ45 is a Python IRC bot based on [CloudBot](http://github.com/ClouDev/CloudBot) by [ClouDev].

## Getting and using RJ45

### Download

Get RJ45 at [https://github.com/allanice001/RJ45](https://github.com/allanice001/RJ45" "Get CloudBot from Github!").

Unzip the resulting file, and continue to read this document.

### Install

Before you can run the bot, you need to install a few Python dependencies. LXML is required while Enchant and PyDNS are needed for several plugins.


These can be installed with `pip` (The Python package manager):

    [sudo] pip install -r requirements.txt

### Run

Before you run the bot, rename `config.default` to `config` and edit it with your preferred settings.

Once you have installed the required dependencies and renamed the config file, you can run the bot! Make sure you are in the correct folder and run the following command:

`python bot.py`

## Getting help with RJ45

### Documentation

To configure your RJ45, visit the [Config Page](http://RJ45.linaccess.com/wiki/RJ45-ircconfig).

To write your own plugins, visit the [Plugin Wiki Page](http://RJ45.linaccess.com/wiki/RJ45-ircplugins).

More at the [Wiki Main Page](http://RJ45.linaccess.com/).

### Support

The developers reside at support.linaccess.com and would be glad to help you.

If you think you have found a bug/have a idea/suggestion, please **open a issue** here on Github.

### Requirements

RJ45 runs on **Python** *2.7.x*.

It **requires the Python module** lXML.
The module `Enchant` is needed for the spellcheck plugin.
The module `PyDNS` is needed for SRV record lookup in the mcping plugin.

## License

RJ45 is **licensed** under the **GPL v2** license. The terms are as follows.

    RJ45

    Copyright © 2013 Allan Swanepoel

    RJ45 is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    RJ45 is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with RJ45.  If not, see <http://www.gnu.org/licenses/gpl-2.0.html>.

