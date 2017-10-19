from tests.syntax import *

# Functional-programming-related
PARTIAL = symbol("curry")
CHAIN =   symbol("chain")

# List-related
MAP =             symbol("map")
FILTER =          symbol("filter")
REDUCE =          symbol("reduce")
GET_ELEMENT =     symbol("element")
APPEND_ELEMENT =  symbol("append")
PREPEND_ELEMENT = symbol("prepend")
CONCATENATE =     symbol("concatenate")
FIRST_ELEMENT =   symbol("first")
LAST_ELEMENT =    symbol("last")
ALL_BUT_FIRST =   symbol("all-but-first")
ALL_BUT_LAST =    symbol("all-but-last")
LENGTH =          symbol("length")

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

# Loop-related
TIMES   = symbol("times")
ITERATE = symbol("iterate")

# Comparisons
ARE_EQUAL =             symbol("=")
GREATER_THAN =          symbol(">")
GREATER_THAN_OR_EQUAL = symbol(">=")
LESS_THAN =             symbol("<")
LESS_THAN_OR_EQUAL =    symbol("<=")


