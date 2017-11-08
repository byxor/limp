import limp.errors as Errors
import limp.internal_types.helpers as Helpers
from limp.internal_types.form import Form


class Function(Form):

    KEYWORD = 'function'
    SELF_REFERENCE = 'this'

    def is_valid(self):
        return self._contents[0] == Function.KEYWORD

    def evaluate(self):

        child_environment = self._environment

        if len(self._contents) > 2:
            argument_names = self._contents[1]
            body_contents = self._contents[2]
        else:
            argument_names = []
            body_contents = self._contents[1]

        def __internal_function(*called_with):
            execution_environment = child_environment.new_child()
            _bind_parameters(execution_environment, argument_names, called_with)
            execution_environment.define(Function.SELF_REFERENCE, __internal_function)
            output = Helpers.evaluate(body_contents, execution_environment)
            return output

        return __internal_function


def _bind_parameters(execution_environment, names, values):
    for name, value in zip(names, values):
        execution_environment.define(name, value)


class ShorthandFunction(Form):

    KEYWORD = '->'

    def is_valid(self):
        if len(self._contents) < 2:
            return False
        keyword_index = -2
        return self._contents[keyword_index] == ShorthandFunction.KEYWORD

    def evaluate(self):
        return self.__internal_form().evaluate()

    def __internal_form(self):
        parameter_names = self._contents[:-2]
        body = self._contents[-1]
        contents = [
            Function.KEYWORD,
            parameter_names,
            body,
        ]
        return Function(contents, self._environment)


class Invocation(Form):

    def is_valid(self):
        return isinstance(self._contents, list)

    def evaluate(self):
        function = Helpers.evaluate(self._contents[0], self._environment)
        arguments = Helpers.evaluate_list_of(self._contents[1:], self._environment)
        return function(*arguments)


class SimpleConditional(Form):

    KEYWORD = 'if'

    def is_valid(self):
        return self._contents[0] == SimpleConditional.KEYWORD

    def evaluate(self):
        outcome = Helpers.evaluate(self._contents[1], self._environment)
        return self.__get_result_for(outcome)

    def __get_result_for(self, outcome):
        if outcome == True:
            return Helpers.evaluate(self._contents[2], self._environment)
        elif outcome == False:
            if self.__else_form_supplied():
                return Helpers.evaluate(self._contents[3], self._environment)

    def __else_form_supplied(self):
        MINIMUM_NUMBER_OF_CONTENTS = 4
        return len(self._contents) >= MINIMUM_NUMBER_OF_CONTENTS


class ComplexConditional(Form):

    KEYWORD = 'condition'

    def is_valid(self):
        return self._contents[0] == ComplexConditional.KEYWORD

    def evaluate(self):
        pairs = self._contents[1:]
        for pair in pairs:
            outcome = Helpers.evaluate(pair[0], self._environment)
            if outcome:
                return Helpers.evaluate(pair[1], self._environment)


class SequentialEvaluator(Form):

    KEYWORD = 'do'

    def is_valid(self):
        return self._contents[0] == SequentialEvaluator.KEYWORD

    def evaluate(self):
        nodes = self._contents[1:]
        if len(nodes) <= 1:
            raise Errors.UnnecessarySequentialEvaluator()
        for node in nodes:
            result = Helpers.evaluate(node, self._environment)
        return result


class Definition(Form):

    KEYWORD = 'define'

    def is_valid(self):
        return self._contents[0] == Definition.KEYWORD

    def evaluate(self):
        name = self._contents[1]
        value = Helpers.evaluate(self._contents[2], self._environment)
        self._environment.define(name, value)
