from typing import Dict
from types import ModuleType
from importlib import import_module

from logger.interface_logger import if_logger
from interfaces.resolver import interface_resolver
from plugins.resolver import get_registered_plugins_for

def validate_context(execution_context):
    return True


def launch_interface(execution_context: Dict, interface_args: Dict):

    if validate_context(execution_context):

        if_name = execution_context['interface_name']
        if_ver = execution_context['interface_version']
        cust = execution_context['customer']

        if_fn = interface_resolver(if_name, if_ver)

        ctx = execution_context.copy()
        ctx['plugins'] = get_registered_plugins_for(if_name, cust, if_ver)

        if if_fn:
            if_fn(ctx=ctx, **interface_args)
        else:
            if_logger.error(f'Failed to resolve entrypoint for {if_name}!')

    else:
        if_logger.error(f'Invalid context!')
