import operator
import math


Environment = dict


def create_empty():
    return Environment()


def create_standard():
    environment = Environment()
    environment.update(_mathematical_functions())
    environment.update(_comparison_functions())
    return environment


def _mathematical_functions():
    return {
        '+':    operator.add,
        '-':    operator.sub,
        '*':    operator.mul,
        '/':    operator.truediv,
        '//':   operator.floordiv,
        '**':   operator.pow,
        '%':    operator.mod,
        'sqrt': math.sqrt,
        '!':    math.factorial,
    }


def _comparison_functions():
    return {
        '=':  operator.eq,
        '>':  operator.gt,
        '<':  operator.lt,
        '<=': operator.le,
        '>=': operator.ge,
    }
