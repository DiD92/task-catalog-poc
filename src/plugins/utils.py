
def plugin_config(ver: int, slot: int):
    def wrapper(f):
        setattr(f, 'ver', ver)
        setattr(f, 'slot', slot)

        return f

    return wrapper


def call_if_present(ctx, slot: int, **kwargs):
    if slot in ctx['plugins'].keys():
        return (True, ctx['plugins'][0](ctx, **kwargs))

    return (False, None)
