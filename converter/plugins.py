import sys
import importlib
import inspect
import pkgutil


def list_plugins():
    plugins = importlib.import_module("plugins")
    for module in pkgutil.iter_modules(plugins.__path__, plugins.__name__ + "."):
        yield importlib.import_module(module.name)


def load_plugins():
    # Dynamically Load Plugins
    for plugin in list_plugins():
        if hasattr(plugin, "register_multirecord"):
            plugin.register_multirecord()
