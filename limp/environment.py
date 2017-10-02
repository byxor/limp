import limp.errors as Errors
import operator
import math
from functional import seq


def create_empty():
    return _Environment()


def create_standard():
    environment = _Environment()
    modules = [
        _mathematical_functions,
        _comparison_functions,
        _boolean_functions,
        _string_functions,
        _easter_egg_symbols,
        _looping_functions,
        _list_functions,
        _conversion_functions,
        _shared_functions,
    ]
    for module in modules:
        symbols = module()
        environment.define_batch_of(symbols)
    return environment


def _mathematical_functions():
    return {
        '+':    lambda *args: seq(args).reduce(operator.add),
        '-':    lambda *args: seq(args).reduce(operator.sub),
        '*':    lambda *args: seq(args).reduce(operator.mul),
        '/':    lambda *args: seq(args).reduce(operator.truediv),
        '//':   lambda *args: seq(args).reduce(operator.floordiv),
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
        'strip':       lambda s: s.strip(),
        'length':      lambda s: len(s),
        'in':          lambda a, b: a in b,
        'repeat':      lambda s, amount: s * amount,
        'reverse':     lambda s: s[::-1],
        'lowercase':   lambda s: s.lower(),
        'uppercase':   lambda s: s.upper(),
    }


def _looping_functions():
    return {
        'times': _times,
        'iterate': _iterate,
    }


def _times(iterations, callback):
    for _ in range(iterations): callback()


def _iterate(iterations, callback):
    for i in range(iterations): callback(i)

    
def _list_functions():
    return {
        'map':           lambda elements, function: list(map(function, elements)),
        'filter':        lambda elements, function: list(filter(function, elements)),
        'element':       lambda elements, index: elements[index],
        'append':        _append,
        'first':         lambda elements: elements[0],
        'last':          lambda elements: elements[-1],
        'all-but-first': lambda elements: elements[1:],
        'all-but-last':  lambda elements: elements[:-1],
    }


def _append(elements, element):
    elements.append(element)
    return elements


def _shared_functions():
    return {
        'concatenate': _concatenate,
    }


def _concatenate(*args):
    first = args[0]
    second = args[1]
    rest = args[1:]
    count = len(args)
    if type(first) == list:
        concatenated = first
        if count <= 2:
            for arg in second:
                concatenated.append(arg)
        else:
            for arg in rest:
                concatenated.append(arg)
        return concatenated
    else:
        return seq(args).map(str).reduce(operator.add)


def _conversion_functions():
    return {
        'integer': int,
        'string':  str,
        'float':   float,
        'boolean': lambda b: b == "true"
    }
    


def _easter_egg_symbols():
    return {
        'bizkit': "Keep ROLLIN ROLLIN ROLLIN ROLLIN whaaat!",
    }


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
