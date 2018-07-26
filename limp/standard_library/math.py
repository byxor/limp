import math
import operator
from functional import seq

ADD = "+"
SUBTRACT = "-"
MULTIPLY = "*"
DIVIDE = "/"
INTEGER_DIVIDE = "//"
MODULO = "%"
FACTORIAL = "!"
EXPONENT = "**"
SQUARE_ROOT = "square-root"
IS_DIVISOR = "divisor?"
IS_EVEN = "even?"
IS_ODD = "odd?"


def symbols():
    return {
        ADD: lambda *args: seq(args).reduce(operator.add),
        SUBTRACT: lambda *args: seq(args).reduce(operator.sub),
        MULTIPLY: lambda *args: seq(args).reduce(operator.mul),
        DIVIDE: lambda *args: seq(args).reduce(operator.truediv),
        INTEGER_DIVIDE: lambda *args: seq(args).reduce(operator.floordiv),
        EXPONENT: operator.pow,
        MODULO: operator.mod,
        FACTORIAL: math.factorial,
        SQUARE_ROOT: math.sqrt,
        IS_DIVISOR: _divisor,
        IS_EVEN: _even,
        IS_ODD: _odd,
    }


def _divisor(potential_divisor, number):
    return number % potential_divisor == 0


def _even(number):
    return _divisor(2, number)


def _odd(number):
    return not _even(number)
