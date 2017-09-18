class Symbol:

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def evaluate(self):
        name = self.__contents
        return self.__environment[name]

    def is_valid(self):
        return type(self.__contents) == str
