import limp.errors as Errors
from functional import seq


class NullOperation:
    def evaluate(self):
        return None


class Function:

    KEYWORD = 'function'
    
    def __init__(self, contents, environment):
        self.__contents = contents
        self.__child_environment = environment.new_child()

    def is_valid(self):
        return self.__contents[0] == Function.KEYWORD

    def evaluate(self):
        from limp.types import Form
        argument_names = self.__contents[1]
        body_contents = self.__contents[2]
        
        def __internal_function(*called_with):
            execution_environment = self.__child_environment.new_child()
            self.__bind_parameters(execution_environment, argument_names, called_with)
            executable_form = Form.infer_from(body_contents, execution_environment)
            function_output = executable_form.evaluate()
            return function_output
        
        return __internal_function

    def __bind_parameters(self, execution_environment, names, values):
        for name, value in zip(names, values):
            execution_environment.define(name, value)


class Invocation:

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        return type(self.__contents) == list
        
    def evaluate(self):
        function_node = self.__contents[0]
        function = self.__to_form(function_node).evaluate()
        argument_nodes = self.__contents[1:]
        arguments = (seq(argument_nodes)
                     .map(self.__to_form)
                     .map(self.__evaluated))
        return function(*arguments)

    def __to_form(self, node):
        from limp.types import Form
        return Form.infer_from(node, self.__environment)

    def __evaluated(self, form):
        return form.evaluate()

    

class Conditional:

    KEYWORD = 'if'

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        return self.__contents[0] == Conditional.KEYWORD

    def evaluate(self):
        condition = self.__new_form(self.__contents[1])
        outcome = condition.evaluate()
        result_form = self.__get_result_form_for(outcome)
        return result_form.evaluate()

    def __new_form(self, contents):
        from limp.types import Form
        return Form.infer_from(contents, self.__environment)

    def __get_result_form_for(self, outcome):
        form = NullOperation()
        if outcome == True:
            form = self.__new_form(self.__contents[2])
        elif outcome == False:
            if self.__else_form_supplied():
                form = self.__new_form(self.__contents[3])
        return form
    
    def __else_form_supplied(self):
        return len(self.__contents) >= 4



class SequentialEvaluator:

    KEYWORD = 'do'

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        return self.__contents[0] == SequentialEvaluator.KEYWORD
        
    def evaluate(self):
        from limp.types import Form
        forms = self.__contents[1:]
        if len(forms) <= 1:
            raise Errors.UnnecessarySequentialEvaluator()
        for node in forms:
            form = Form.infer_from(node, self.__environment)
            result = form.evaluate()
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
        value = Form.infer_from(self.__contents[2], self.__environment).evaluate()
        self.__environment.define(name, value)
        
