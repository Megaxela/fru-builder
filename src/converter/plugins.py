from importlib import import_module
from pkgutil import iter_modules


def list_plugins():
    plugins = import_module("plugins")
    for module in iter_modules(plugins.__path__, plugins.__name__ + "."):
        yield import_module(module.name)


def load_plugins():
    # Dynamically Load Plugins
    for plugin in list_plugins():
        if hasattr(plugin, "register_multirecord"):
            plugin.register_multirecord()
