from importlib import import_module

PYTHON_MODULE_NAMES = [
    "meta",
    "objects",
    "math",
    "comparisons",
    "conversions",
    "conditions",
    "booleans",
    "strings",
    "lists",
    "loops",
    "functional",
    "shared",
    "easter_eggs",
]


def symbols():
    symbols = []
    for python_module_name in PYTHON_MODULE_NAMES:
        python_module = import_module(_absolute_path(python_module_name))
        module_symbols = python_module.symbols()
        symbols += module_symbols.items()
    return symbols


def _absolute_path(module_name):
    return f"limp.standard_library.{module_name}"
