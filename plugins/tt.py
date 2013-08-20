from util import hook

@hook.command
def tt(inp):
    "tt <number> -- Returns a link to a tt."

    return 'TT: http://tt/'+inp
