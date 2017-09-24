import limp.errors as Errors


class Symbol:

    def __init__(self, contents, environment):
        self.__name = contents
        self.__environment = environment

    def evaluate(self):
        return self.__environment.resolve(self.__name)

    def is_valid(self):
        contents = self.__name
        return type(contents) == str


class String:

    DELIMITER = '"'
    
    def __init__(self, contents, environment):
        self.__contents = contents

    def is_valid(self):
        return self.__is_long_enough() and \
        self.__is_surrounded_by_delimiters() and \
        self.__has_correct_delimiter_count()

    def evaluate(self):
        return self.__contents[1:-1]

    def __is_long_enough(self):
        return len(self.__contents) >= 2
    
    def __is_surrounded_by_delimiters(self):
        start = self.__contents[0] == String.DELIMITER
        end = self.__contents[-1] == String.DELIMITER
        return start and end

    def __has_correct_delimiter_count(self):
        return True
