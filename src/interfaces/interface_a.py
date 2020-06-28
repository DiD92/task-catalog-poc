
from interfaces.utils import slot_config
from logger.interface_logger import if_logger
from plugins.utils import call_if_present


@slot_config(config={
    0: {
        "include_ctx": True,
        "include_kwargs": True,
        "mandatory_args": {
            "a": int,
            "b": float
        },
        "returns": False,
        "return_type": None
    }
})
def interface_a_entrypoint_v1(ctx, arg1, **kwargs):
    print(f'Hi! I\'m interface A version 1! This are my args: {arg1} {kwargs}')

    plugin_present, result = call_if_present(ctx, 0, kwargs={})

def interface_a_entrypoint_v2(ctx, arg1, **kwargs):
    print(f'Hi! I\'m interface A version 1! This are my args: {arg1} {kwargs}')

def interface_a_entrypoint_v3(ctx, arg1, **kwargs):
    print(f'Hi! I\'m interface A version 1! This are my args: {arg1} {kwargs}')
