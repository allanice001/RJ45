from util import hook

@hook.command
def customer(inp):
    "customer <email / acc#:> -- Returns a link to SOT for a customer."

    return 'Customer: https://aws-tools.amazon.com/servicetools/search.aws?searchType=ACCOUNT&query='+inp
