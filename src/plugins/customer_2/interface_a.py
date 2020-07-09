from typing import Dict, Any

from plugins.utils import plugin_config

@plugin_config(ver=1, slot=0)
def plugin_1(ctx: Dict[str, Any], a: int, b: float, **kwargs):
    print('Hi! I\'m a plugin in interface_a for customer_2!')

    return a / b
