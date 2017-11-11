import limp.internal_types.helpers as Helpers
import limp.environment as Environment
import limp.internal_types.form as Form


class Symbol(Form.Constructor):

    def is_valid(self):
        return isinstance(self._contents, str)

    def evaluate(self):
        name = self._contents
        return self._environment.resolve(name)


class String(Form.Constructor):

    DELIMITER = '"'

    def is_valid(self):
        return self.__is_long_enough() and \
        self.__is_surrounded_by_delimiters()

    def evaluate(self):
        return self.__discard_delimiters()

    def __is_long_enough(self):
        return len(self._contents) >= 2

    def __is_surrounded_by_delimiters(self):
        start = self._contents[0] == String.DELIMITER
        end = self._contents[-1] == String.DELIMITER
        return start and end

    def __discard_delimiters(self):
        return self._contents[1:-1]


class List(Form.Constructor,
           Form.create_keyword_validity_checker()):

    KEYWORD = 'list'
    OPEN_DELIMITER = '['
    CLOSE_DELIMITER = ']'

    def evaluate(self):
        element_nodes = self._contents[1:]
        return Helpers.evaluate_list_of(element_nodes, self._environment)


class Object(Form.Constructor,
             Form.create_keyword_validity_checker()):

    KEYWORD = 'object'

    def evaluate(self):
        object_ = Environment.create_empty()
        attributes = self._contents[1:]
        for name, value_node in attributes:
            value = Helpers.evaluate(value_node, self._environment)
            object_.define(name, value)
        return object_
