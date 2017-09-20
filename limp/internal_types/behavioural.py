from functional import seq


class NullOperation:
    def evaluate(self):
        return None


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
        
