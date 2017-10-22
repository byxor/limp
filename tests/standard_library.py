from tests.syntax import *

# Functional-programming-related
PARTIAL = symbol("curry")
CHAIN =   symbol("chain")

LIST_MAP =             symbol("map")
LIST_FILTER =          symbol("filter")
LIST_REDUCE =          symbol("reduce")
LIST_GET_ELEMENT =     symbol("element")
LIST_APPEND_ELEMENT =  symbol("append")
LIST_PREPEND_ELEMENT = symbol("prepend")
LIST_CONCATENATE =     symbol("concatenate")
LIST_FIRST_ELEMENT =   symbol("first")
LIST_LAST_ELEMENT =    symbol("last")
LIST_ALL_BUT_FIRST =   symbol("all-but-first")
LIST_ALL_BUT_LAST =    symbol("all-but-last")
LIST_LENGTH =          symbol("length")

# Math-related
ADD =            symbol("+")
SUBTRACT =       symbol("-")
MULTIPLY =       symbol("*")
DIVIDE =         symbol("/")
INTEGER_DIVIDE = symbol("//")
MODULO =         symbol("%")
FACTORIAL =      symbol("!")
EXPONENT =       symbol("**")
SQUARE_ROOT =    symbol("sqrt")
IS_DIVISOR =     symbol("divisor?")
IS_EVEN =        symbol("even?")
IS_ODD =         symbol("odd?")

# Boolean-related
AND = symbol("and")
OR  = symbol("or")
NOT = symbol("not")
XOR = symbol("xor")

STRING_CONCATENATE = symbol("concatenate")
STRING_STRIP =       symbol("strip")
STRING_LENGTH =      symbol("length")
STRING_CONTAINS =    symbol("contains?")
STRING_EMPTY =       symbol("empty?")
STRING_REPEAT =      symbol("repeat")
STRING_REVERSE =     symbol("reverse")
STRING_LOWERCASE =   symbol("lowercase")
STRING_UPPERCASE =   symbol("uppercase")
STRING_SPLIT =       symbol("split")
STRING_JOIN =        symbol("join-string")

# Loop-related
TIMES   = symbol("times")
ITERATE = symbol("iterate")

# Conversions
STRING =  symbol("string")
INTEGER = symbol("integer")
FLOAT =   symbol("float")
BOOLEAN = symbol("boolean")

# Comparisons
ARE_EQUAL =             symbol("=")
GREATER_THAN =          symbol(">")
GREATER_THAN_OR_EQUAL = symbol(">=")
LESS_THAN =             symbol("<")
LESS_THAN_OR_EQUAL =    symbol("<=")
