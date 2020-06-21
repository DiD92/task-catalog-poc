from importlib import import_module

from logger.interface_logger import if_logger


def get_registered_plugins_for(if_name: str, customer: str, version: int):
    plugin_dict = {}

    try:
        p_mod = import_module(f'plugins.{customer}.{if_name}')

        plugin_set = [f for _, f in p_mod.__dict__.items()
                      if _is_valid_plugin(f)]

        plugin_set = [f for f in plugin_set if f.ver == version]

        plugin_dict = {f.slot: f for f in plugin_set}

    except ModuleNotFoundError:
        pass

    if_logger.info(
        f'Found {len(plugin_dict)} plugins registered for {if_name}_v{version} on customer {customer}')
    
    return plugin_dict


def _is_valid_plugin(module_item):
    return callable(module_item) and hasattr(module_item, 'ver') and hasattr(module_item, 'slot')
