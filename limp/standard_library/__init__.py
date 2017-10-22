from importlib import import_module


PYTHON_MODULE_NAMES = [
    "math",
    "comparisons",
    "conversions",
    "booleans",
    "strings",
    "lists",
    "loops",
    "functional",
    "shared",
    "easter_eggs",
]


def symbols():
    symbols = dict()
    for python_module_name in PYTHON_MODULE_NAMES:
        python_module = import_module(_absolute_path(python_module_name))
        module_symbols = python_module.symbols()
        symbols.update(module_symbols)
    return symbols


def _absolute_path(module_name):
    return f"limp.standard_library.{module_name}"
