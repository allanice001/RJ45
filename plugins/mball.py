from util import hook, text
import random

color_codes = {
    "<r>": "\x02\x0305",
    "<g>": "\x02\x0303",
    "<y>": "\x02"
}

with open("plugins/data/mball_responses.txt") as f:
    responses = [line.strip() for line in
        f.readlines()if not line.startswith("//")]

# @hook.command('8ball')
@hook.command
def mball(input, me=None):
    "mball <question> -- The all knowing magic eight ball, " \
    "in electronic form. Ask and it shall be answered!"

    magic = text.multiword_replace(random.choice(responses), color_codes)
    me("shakes the magic 8 ball... %s" % magic)

