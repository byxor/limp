import functools
import limp.errors as Errors
import limp.standard_library as StandardLibrary
import operator
import math
from functional import seq


def create_empty():
    return _Environment()


def create_standard():
    environment = _Environment()
    environment.define_batch_of(StandardLibrary.symbols())
    return environment


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
        for name, value in symbols:
            self.define(name, value)
            
    def new_child(self):
        return _Environment(self)
        
