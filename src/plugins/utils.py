
def plugin_config(ver: int, slot: int):
    def wrapper(f):
        setattr(f, 'ver', ver)
        setattr(f, 'slot', slot)

        return f

    return wrapper


def call_if_present(context, plugin_slot: int, *args, **kwargs):
    if plugin_slot in context['plugins'].keys():
        plugin_fn = context['plugins'][plugin_slot]
        return (True, plugin_fn(context, *args, **kwargs))

    return (False, None)
