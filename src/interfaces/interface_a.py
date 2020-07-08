
from interfaces.utils import slot_config
from logger.interface_logger import if_logger
from plugins.utils import call_if_present as cip


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
def interface_a_entrypoint_v1(ctx, arg1: int, **kwargs):
    print(f'Hi! I\'m interface A version 1! This are my args: {arg1}, and kwargs: {kwargs}')

    param_a = 10
    param_b = 8.0

    plugin_found, result = cip(ctx, 0, param_a, param_b)

    return result + arg1


def interface_a_entrypoint_v2(ctx, arg1, **kwargs):
    print(f'Hi! I\'m interface A version 1! This are my args: {arg1} {kwargs}')


def interface_a_entrypoint_v3(ctx, arg1, **kwargs):
    print(f'Hi! I\'m interface A version 1! This are my args: {arg1} {kwargs}')
