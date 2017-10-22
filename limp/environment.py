import functools
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
        _functional_functions
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

        'divisor?': _divisor,
        'even?':    _even,
        'odd?':     _odd,
    }


def _divisor(potential_divisor, number):
    return number % potential_divisor == 0


def _even(number):
    return _divisor(2, number)


def _odd(number):
    return not _even(number)
    

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
        'empty?':      lambda s: len(s) == 0, 
        'contains?':   lambda a, b: b in a,
        'repeat':      lambda s, amount: s * amount,
        'reverse':     lambda s: s[::-1],
        'lowercase':   lambda s: s.lower(),
        'uppercase':   lambda s: s.upper(),
        'split':       lambda delimiter, string: string.split(delimiter),
        'join-string': lambda separator, list_: separator.join(list_),
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
        'map':           lambda function, elements: seq(elements).map(function),
        'filter':        lambda function, elements: seq(elements).filter(function),
        'reduce':        lambda function, elements: seq(elements).reduce(function),
        'element':       lambda elements, index: elements[index],
        'append':        _append,
        'prepend':       _prepend,
        'first':         lambda elements: elements[0],
        'last':          lambda elements: elements[-1],
        'all-but-first': lambda elements: elements[1:],
        'all-but-last':  lambda elements: elements[:-1],
    }


def _append(elements, element):
    copy = elements[::]
    copy.append(element)
    return copy


def _prepend(elements, element):
    return [element] + elements


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
        concatenated = first[::]
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
        'boolean': _boolean,
    }


def _boolean(x):
    if type(x) == str:
        import limp.types as Types
        return x == Types.Boolean.TRUE_KEYWORD
    else:
        return bool(x)


def _functional_functions():
    return {
        'chain': _chain,
        'curry': _curry,
    }


def _chain(input_, *functions):
    output = input_
    for function in functions:
        output = function(output)
    return output


def _curry(function, *early_arguments):
    return lambda *late_arguments: function(*early_arguments, *late_arguments)


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
        
