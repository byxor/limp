from functional import seq


class SequentialEvaluator:

    KEYWORD = 'do'

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        return self.__contents[0] == SequentialEvaluator.KEYWORD
        
    def evaluate(self):
        from limp.types import Form
        for node in self.__contents[1:]:
            form = Form.infer_from(node, self.__environment)
            form.evaluate()        



class Invocation:

    def __init__(self, contents, environment):
        self.__contents = contents
        self.__environment = environment

    def is_valid(self):
        return type(self.__contents) == list
        
    def evaluate(self):
        function = self.__environment[self.__contents[0]]
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
        
