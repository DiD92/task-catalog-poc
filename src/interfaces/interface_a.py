
from logger.interface_logger import if_logger
from plugins.utils import call_if_present

def interface_a_entrypoint_v1(ctx, arg1, **kwargs):
    print(f'Hi! I\'m interface A version 1! This are my args: {arg1} {kwargs}')

    plugin_present, result = call_if_present(ctx, 0, kwargs={})

def interface_a_entrypoint_v2(ctx, arg1, **kwargs):
    print(f'Hi! I\'m interface A version 1! This are my args: {arg1} {kwargs}')

def interface_a_entrypoint_v3(ctx, arg1, **kwargs):
    print(f'Hi! I\'m interface A version 1! This are my args: {arg1} {kwargs}')
