from util import hook

@hook.command
@hook.command('smokebreak')
def smoke(inp):
    'Time for a smoke break?'
    return 'Smoke break coming up. Anyone else wanna join '+inp
