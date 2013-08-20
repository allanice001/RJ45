from util import hook

@hook.command
def coffee(inp):
    'Time for a break? How about some Coffee?'
    return 'Coffee Run coming up. Anyone else wanna join '+inp
