import limp.errors as Errors
import limp.internal_types.helpers as Helpers
import limp.environment as Environment
from functional import seq


class Symbol:

    def __init__(self, contents, environment):
        self.__name = contents
        self.__environment = environment

    def is_valid(self):
        contents = self.__name
        return type(contents) == str
        
    def evaluate(self):
        return self.__environment.resolve(self.__name)


class String:

    DELIMITER = '"'
    
    def __init__(self, contents, environment):
        self.__contents = contents

    def is_valid(self):
        return self.__is_long_enough() and \
        self.__is_surrounded_by_delimiters() and \
        self.__has_correct_delimiter_count()

    def evaluate(self):
        string = self.__contents[1:-1]
        return string

    def __is_long_enough(self):
        return len(self.__contents) >= 2
    
    def __is_surrounded_by_delimiters(self):
        start = self.__contents[0] == String.DELIMITER
        end = self.__contents[-1] == String.DELIMITER
        return start and end

    def __has_correct_delimiter_count(self):
        return True


class List:

    KEYWORD = 'list'
    OPEN_DELIMITER = '['
    CLOSE_DELIMITER = ']'
    
    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        return self.__contents[0] == List.KEYWORD

    def evaluate(self):
        nodes = self.__contents[1:]
        return Helpers.evaluate_list_of(nodes, self.__environment)


class Object:

    KEYWORD = 'object'

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        return self.__contents[0] == Object.KEYWORD

    def evaluate(self):
        object_ = Environment.create_empty()
        attributes = self.__contents[1:]
        for name, value_node in attributes:
            value = Helpers.evaluate(value_node, self.__environment)
            object_.define(name, value)
        return object_
            
        
