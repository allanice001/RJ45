from util import hook

@hook.command
def case(inp):
    "case <case number> -- Returns a yuma link to a case."

    return 'Case: http://tiny/r7ig64zn/'+inp
