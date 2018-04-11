import limp.errors as Errors
import limp.internal_types.helpers as Helpers
import limp.internal_types.form as Form


class Function(Form.Constructor,
               Form.create_keyword_validity_checker(-2)):

    KEYWORD = '->'
    SELF_REFERENCE = 'this'

    def evaluate(self):
        parameter_names = self._contents[:-2]
        body_contents = self._contents[-1]

        def internal_function(*parameter_values):
            execution_environment = self._environment.new_child()
            parameters = zip(parameter_names, parameter_values)

            _bind(parameters, execution_environment)
            _apply_self_reference(internal_function, execution_environment)

            output = Helpers.evaluate(body_contents, execution_environment)
            return output

        return internal_function

    def __get_parameter_names(self):
        return self._contents[1] if self.__has_arguments() else []

    def __has_arguments(self):
        return len(self._contents) > 2


def _bind(parameters, execution_environment):
    for name, value in parameters:
        execution_environment.define(name, value)


def _apply_self_reference(function, execution_environment):
    execution_environment.define(Function.SELF_REFERENCE, function)




class Invocation(Form.Constructor):

    def is_valid(self):
        return isinstance(self._contents, list)

    def evaluate(self):
        try:
            function = Helpers.evaluate(self._contents[0], self._environment)
            parameters = Helpers.evaluate_list_of(self._contents[1:], self._environment)
            return function(*parameters)
        except IndexError:
            raise Errors.EmptyInvocation()


class SimpleConditional(Form.Constructor,
                        Form.create_keyword_validity_checker()):

    KEYWORD = 'if'

    def evaluate(self):
        outcome = Helpers.evaluate(self._contents[1], self._environment)
        return self.__get_result_for(outcome)

    def __get_result_for(self, outcome):
        if outcome == True:
            return Helpers.evaluate(self._contents[2], self._environment)
        elif outcome == False:
            if self.__else_body_supplied():
                return Helpers.evaluate(self._contents[3], self._environment)

    def __else_body_supplied(self):
        MINIMUM_NUMBER_OF_CONTENTS = 4
        return len(self._contents) >= MINIMUM_NUMBER_OF_CONTENTS


class ComplexConditional(Form.Constructor,
                         Form.create_keyword_validity_checker()):

    KEYWORD = 'condition'

    def evaluate(self):
        pairs = self._contents[1:]
        for pair in pairs:
            outcome = Helpers.evaluate(pair[0], self._environment)
            if outcome:
                return Helpers.evaluate(pair[1], self._environment)


class SequentialEvaluator(Form.Constructor,
                          Form.create_keyword_validity_checker()):

    KEYWORD = 'do'

    def evaluate(self):
        nodes = self._contents[1:]
        if len(nodes) <= 1:
            raise Errors.UnnecessarySequentialEvaluator()
        for node in nodes:
            result = Helpers.evaluate(node, self._environment)
        return result


class Definition(Form.Constructor, Form.create_keyword_validity_checker()):

    KEYWORD = 'define'

    def evaluate(self):
        name = self._contents[1]
        value = Helpers.evaluate(self._contents[2], self._environment)
        self._environment.define(name, value)
