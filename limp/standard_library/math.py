import math
import operator
from functional import seq


def symbols():
    return {
        '+':  lambda *args: seq(args).reduce(operator.add),
        '-':  lambda *args: seq(args).reduce(operator.sub),
        '*':  lambda *args: seq(args).reduce(operator.mul),
        '/':  lambda *args: seq(args).reduce(operator.truediv),
        '//': lambda *args: seq(args).reduce(operator.floordiv),
        '**': operator.pow,
        '%':  operator.mod,
        '!':  math.factorial,
        'sqrt':     math.sqrt,
        'divisor?': _divisor,
        'even?':    _even,
        'odd?':     _odd,
    }


def _divisor(potential_divisor, number):
    return number % potential_divisor == 0


def _even(number): return _divisor(2, number)


def _odd(number): return not _even(number)
    
