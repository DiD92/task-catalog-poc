from typing import Dict, Any
from types import ModuleType
from importlib import import_module
from inspect import signature, Parameter

from logger.interface_logger import if_logger
from interfaces.resolver import interface_resolver
from plugins.resolver import get_registered_plugins_for


def validate_context(execution_context):
    return True


def validate_plugins_for(interface_fn, plugin_set):
    if not hasattr(interface_fn, 'slots'):
        if_logger.warning(f'Plugin config not found for: {interface_fn}!')
        return {}

    slot_config = getattr(interface_fn, 'slots')

    for slot_index, cfg in slot_config.items():
        sig_config = {'params': {}, 'returns': None}
        if 'include_ctx' in cfg:
            sig_config['params']['ctx'] = Dict[str, Any]

        for arg_name, arg_annotation in cfg.get('mandatory_args', {}).items():
            sig_config['params'][arg_name] = arg_annotation

        if 'include_kwargs' in cfg:
            sig_config['params']['kwargs'] = None

        if 'returns' in cfg and cfg['returns']:
            sig_config['returns'] = cfg.get('return_type', None)

        slot_config[slot_index] = sig_config

    plugin_types = {}

    for plugin_index, plugin in plugin_set.items():
        plugin_types[plugin_index] = {'params': {}, 'returns': None}

        plugin_sig = signature(plugin)

        plugin_params = plugin_sig.parameters

        p_sdict = {k: None if t.annotation == Parameter.empty else t.annotation
                   for k, t in plugin_params.items()}

        plugin_types[plugin_index]['params'] = p_sdict

        if plugin_sig.return_annotation != Parameter.empty:
            plugin_types[plugin_index]['returns'] = plugin_sig.return_annotation

    valid_plugins = {}

    for plugin_index, plugin in plugin_set.items():

        s_conf = slot_config[plugin_index]
        p_conf = plugin_types[plugin_index]

        if s_conf == p_conf:
            valid_plugins[plugin_index] = plugin
        else:
            if_logger.warning(f'Plugin {plugin_index} for {interface_fn.__name__} has'
                              f' incorrect signature:\n\tExpected: '
                              f'{s_conf}\n\tversus\n\tFound: {p_conf}')

    return valid_plugins


def launch_interface(execution_context: Dict, interface_args: Dict):

    if validate_context(execution_context):

        if_name = execution_context['interface_name']
        if_ver = execution_context['interface_version']
        cust = execution_context['customer']

        if_fn = interface_resolver(if_name, if_ver)

        ctx = execution_context.copy()
        plugin_set = get_registered_plugins_for(if_name, cust, if_ver)

        valid_plugins = validate_plugins_for(if_fn, plugin_set)

        ctx['plugins'] = valid_plugins

        if if_fn:
            if_logger.info(
                f'Launching interface {if_name} with {len(valid_plugins)} valid plugins')
            if_fn(ctx=ctx, **interface_args)
        else:
            if_logger.error(f'Failed to resolve entrypoint for {if_name}!')

    else:
        if_logger.error(f'Invalid context!')
