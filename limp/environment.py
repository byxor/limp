import operator
import math


Environment = dict


def create_empty():
    return Environment()


def create_standard():
    environment = Environment()
    environment.update(_mathematical_functions())
    environment.update(_comparison_functions())
    environment.update(_boolean_functions())
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


def _boolean_functions():
    return {
        'not': lambda x: not x,
        'and': lambda a, b: a and b,
        'or':  lambda a, b: a or b,
        'xor': lambda a, b: (a and not b) or (b and not a)
    }
