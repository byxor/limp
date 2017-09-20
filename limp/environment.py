import operator
import math


Environment = dict


def create_empty():
    return Environment()


def create_standard():
    environment = Environment()
    environment.update(_mathematical_functions())
    return environment


def _mathematical_functions():
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '//': operator.floordiv,
        '**': operator.pow,
        '%': operator.mod,
        'sqrt': math.sqrt,
        '!': math.factorial,
    }
