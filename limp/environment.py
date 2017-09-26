import limp.errors as Errors
import operator
import math
from functional import seq


class _Environment:

    def __init__(self, parent = None):
        self.__parent = parent
        self.__symbols = {}
    
    def define(self, name, value):
        if name in self.__symbols:
            raise Errors.RedefinedSymbol(name)
        else:
            self.__symbols[name] = value

    def resolve(self, name):
        if name in self.__symbols:
            return self.__symbols[name]
        else:
            if self.__parent is not None:
                return self.__parent.resolve(name)
            else:
                raise Errors.UndefinedSymbol(name)

    def define_batch_of(self, symbols):
        self.__symbols.update(symbols)
            
    def new_child(self):
        return _Environment(self)
        
    def __str__(self):
        BORDER_WIDTH = 32
        BORDER_CHARACTER = '-'
        NEW_LINE = '\n'
        BORDER = (BORDER_CHARACTER * BORDER_WIDTH) + NEW_LINE
        s = BORDER
        for name, value in self.__symbols.items():
            s += f'{name}: {value}{NEW_LINE}'
        if self.__parent is not None:
            s += str(self.__parent)
        s += BORDER
        return s


def create_empty():
    return _Environment()


def create_standard():
    environment = _Environment()
    environment.define_batch_of(_mathematical_functions())
    environment.define_batch_of(_comparison_functions())
    environment.define_batch_of(_boolean_functions())
    environment.define_batch_of(_string_functions())
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


def _string_functions():
    return {
        'string': str,
        'concatenate': lambda *args: seq(args).map(str).reduce(operator.add)
    }
