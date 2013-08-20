from util import hook

@hook.command
def k2(inp):
    'Returns a link to K2'
    return 'K2 Link: https://k2.amazon.com/k2/ec2_instances/get?account_id='+inp
