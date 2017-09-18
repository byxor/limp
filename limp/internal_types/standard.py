import limp.errors as Errors


class Symbol:

    def __init__(self, contents, environment):
        self.__name = contents
        self.__environment = environment

    def evaluate(self):
        self.__assert_symbol_exists()
        return self.__environment[self.__name]

    def is_valid(self):
        contents = self.__name
        return type(contents) == str

    def __assert_symbol_exists(self):
        if self.__name not in self.__environment:
            raise Errors.UndefinedSymbol(self.__name)
