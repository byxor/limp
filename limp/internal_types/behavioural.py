import limp.errors as Errors
import limp.internal_types.helpers as Helpers
import inspect
from functional import seq


class Function:

    KEYWORD = 'function'
    SELF_REFERENCE = 'this'
    
    def __init__(self, contents, environment):
        self.__contents = contents
        self.__child_environment = environment.new_child()

    def is_valid(self):
        return self.__contents[0] == Function.KEYWORD

    def evaluate(self):
        from limp.types import Form

        if len(self.__contents) > 2:
            argument_names = self.__contents[1]
            body_contents = self.__contents[2]
        else:
            argument_names = []
            body_contents = self.__contents[1]
        
        def __internal_function(*called_with):
            execution_environment = self.__child_environment.new_child()
            self.__bind_parameters(execution_environment, argument_names, called_with)
            execution_environment.define(Function.SELF_REFERENCE, __internal_function)
            
            executable_form = Form.infer_from(body_contents, execution_environment)
            function_output = executable_form.evaluate()
            return function_output
        
        return __internal_function

    def __bind_parameters(self, execution_environment, names, values):
        for name, value in zip(names, values):
            execution_environment.define(name, value)


class ShorthandFunction:

    KEYWORD = '->'

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        if len(self.__contents) < 2:
            return False
        keyword_index = -2
        return self.__contents[keyword_index] == ShorthandFunction.KEYWORD

    def evaluate(self):
        return self.__internal_form().evaluate()

    def __internal_form(self):
        parameter_names = self.__contents[:-2]
        body = self.__contents[-1]
        contents = [
            Function.KEYWORD,
            parameter_names,
            body,
        ]
        return Function(contents, self.__environment)


class Invocation:

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        return type(self.__contents) == list
        
    def evaluate(self):
        function = Helpers.evaluate(self.__contents[0], self.__environment)
        arguments = Helpers.evaluate_list_of(self.__contents[1:], self.__environment)
        return function(*arguments)


class SimpleConditional:

    KEYWORD = 'if'

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        return self.__contents[0] == SimpleConditional.KEYWORD

    def evaluate(self):
        outcome = Helpers.evaluate(self.__contents[1], self.__environment)
        return self.__get_result_for(outcome)

    def __get_result_for(self, outcome):
        if outcome == True:
            return Helpers.evaluate(self.__contents[2], self.__environment)
        elif outcome == False:
            if self.__else_form_supplied():
                return Helpers.evaluate(self.__contents[3], self.__environment)
    
    def __else_form_supplied(self):
        MINIMUM_NUMBER_OF_CONTENTS = 4
        return len(self.__contents) >= MINIMUM_NUMBER_OF_CONTENTS


class ComplexConditional:

    KEYWORD = 'condition'
    
    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        return self.__contents[0] == ComplexConditional.KEYWORD

    def evaluate(self):
        pairs = self.__contents[1:]
        for pair in pairs:
            outcome = Helpers.evaluate(pair[0], self.__environment)
            if outcome:
                return Helpers.evaluate(pair[1], self.__environment)


class SequentialEvaluator:

    KEYWORD = 'do'

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        return self.__contents[0] == SequentialEvaluator.KEYWORD
        
    def evaluate(self):
        nodes = self.__contents[1:]
        if len(nodes) <= 1:
            raise Errors.UnnecessarySequentialEvaluator()
        for node in nodes:
            result = Helpers.evaluate(node, self.__environment)
        return result


class Definition:

    KEYWORD = 'define'

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        return self.__contents[0] == Definition.KEYWORD
        
    def evaluate(self):
        from limp.types import Form
        name = self.__contents[1]
        value = Helpers.evaluate(self.__contents[2], self.__environment)
        self.__environment.define(name, value)
        
