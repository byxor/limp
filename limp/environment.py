import limp.types as Types
import operator
import math


def create_standard():
    environment = Types.Environment()
    environment.update({
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '//': operator.floordiv,
        '**': operator.pow,
        '%': operator.mod,
        'sqrt': math.sqrt,
        '!': math.factorial,
    })
    return environment
