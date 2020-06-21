from typing import Callable, Optional
from importlib import import_module

from logger.interface_logger import if_logger


def interface_resolver(if_name: str, ver: int) -> Optional[Callable]:

    try:
        if_mod = import_module(f'interfaces.{if_name}')

        if_logger.info(f'Interface {if_name} module {if_mod} found!')

        if _has_entrypoint_for_version(if_mod, if_name, ver):
            if_logger.info(
                f'Found entrypoint for {if_name} with version: {ver}!')
            return _get_entrypoint_for_version(if_mod, if_name, ver)
        else:
            if_logger.warning(
                f'Entrypoint not found for {if_name} with version: {ver}!')
            if _has_entrypoint_for_version(if_mod, if_name, 1):
                if_logger.info(
                    f'Found entrypoint for {if_name} with version: {ver}!')
                return _get_entrypoint_for_version(if_mod, if_name, 1)
            else:
                if_logger.error(
                    f'Entrypoint not found for {if_name} with any version info!')
                return None
    except ModuleNotFoundError:
        if_logger.error(f'Interface {if_name} module not found!')
        return None


def _has_entrypoint_for_version(mod, if_name, version):
    return hasattr(mod, f'{if_name}_entrypoint_v{version}')


def _get_entrypoint_for_version(mod, if_name, version):
    return getattr(mod, f'{if_name}_entrypoint_v{version}')

