class Invocation:

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def evaluate(self):
        from limp.types import Form
        function_name = self.__contents[0]
        function_argument_nodes = self.__contents[1:]
        function_argument_forms = [Form.infer_from(node, self.__environment) for node in function_argument_nodes]
        function_arguments = [form.evaluate() for form in function_argument_forms]
        function = self.__environment[function_name]
        return function(*function_arguments)

    def is_valid(self):
        return type(self.__contents) == list


class Definition:

    KEYWORD = 'define'

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def evaluate(self):
        from limp.types import Form
        variable = self.__contents[1]
        value = Form.infer_from(self.__contents[2], self.__environment).evaluate()
        self.__environment[variable] = value
    
    def is_valid(self):
        return self.__contents[0] == Definition.KEYWORD
        
