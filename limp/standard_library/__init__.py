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
    symbols = []
    for python_module_name in PYTHON_MODULE_NAMES:
        python_module = import_module(_absolute_path(python_module_name))
        module_symbols = python_module.symbols()
        symbols += module_symbols.items()
    return symbols


def _absolute_path(module_name):
    return f"limp.standard_library.{module_name}"


# STANDARD LIBRARY SYMBOL NAMES

# Functional-programming-related
PARTIAL = "curry"
CHAIN =   "chain"

LIST_MAP =             "map"
LIST_FILTER =          "filter"
LIST_REDUCE =          "reduce"
LIST_GET_ELEMENT =     "element"
LIST_APPEND_ELEMENT =  "append"
LIST_PREPEND_ELEMENT = "prepend"
LIST_CONCATENATE =     "concatenate"
LIST_FIRST_ELEMENT =   "first"
LIST_LAST_ELEMENT =    "last"
LIST_ALL_BUT_FIRST =   "all-but-first"
LIST_ALL_BUT_LAST =    "all-but-last"
LIST_LENGTH =          "length"
LIST_CONTAINS =        "contains?"

# Math-related
ADD =            "+"
SUBTRACT =       "-"
MULTIPLY =       "*"
DIVIDE =         "/"
INTEGER_DIVIDE = "//"
MODULO =         "%"
FACTORIAL =      "!"
EXPONENT =       "**"
SQUARE_ROOT =    "sqrt"
IS_DIVISOR =     "divisor?"
IS_EVEN =        "even?"
IS_ODD =         "odd?"

# Boolean-related
AND = "and"
OR  = "or"
NOT = "not"
XOR = "xor"

STRING_CONCATENATE = "concatenate"
STRING_STRIP =       "strip"
STRING_LENGTH =      "length"
STRING_CONTAINS =    "contains?"
STRING_EMPTY =       "empty?"
STRING_REPEAT =      "repeat"
STRING_REVERSE =     "reverse"
STRING_LOWERCASE =   "lowercase"
STRING_UPPERCASE =   "uppercase"
STRING_SPLIT =       "split"
STRING_JOIN =        "join-string"

# Loop-related
TIMES   = "times"
ITERATE = "iterate"

# Conversions
STRING =  "string"
INTEGER = "integer"
FLOAT =   "float"
BOOLEAN = "boolean"

# Comparisons
ARE_EQUAL =             "="
GREATER_THAN =          ">"
GREATER_THAN_OR_EQUAL = ">="
LESS_THAN =             "<"
LESS_THAN_OR_EQUAL =    "<="
