import limp.internal_types.helpers as Helpers
import limp.environment as Environment
from limp.internal_types.form import Form


class Symbol(Form):

    def is_valid(self):
        return isinstance(self._contents, str)

    def evaluate(self):
        name = self._contents
        return self._environment.resolve(name)


class String(Form):

    DELIMITER = '"'

    def is_valid(self):
        return self.__is_long_enough() and \
        self.__is_surrounded_by_delimiters()

    def evaluate(self):
        string = self._contents[1:-1]
        return string

    def __is_long_enough(self):
        return len(self._contents) >= 2

    def __is_surrounded_by_delimiters(self):
        start = self._contents[0] == String.DELIMITER
        end = self._contents[-1] == String.DELIMITER
        return start and end


class List(Form):

    KEYWORD = 'list'
    OPEN_DELIMITER = '['
    CLOSE_DELIMITER = ']'

    def is_valid(self):
        return self._contents[0] == List.KEYWORD

    def evaluate(self):
        nodes = self._contents[1:]
        return Helpers.evaluate_list_of(nodes, self._environment)


class Object(Form):

    KEYWORD = 'object'

    def is_valid(self):
         return self._contents[0] == Object.KEYWORD

    def evaluate(self):
        object_ = Environment.create_empty()
        attributes = self._contents[1:]
        for name, value_node in attributes:
            value = Helpers.evaluate(value_node, self._environment)
            object_.define(name, value)
        return object_
