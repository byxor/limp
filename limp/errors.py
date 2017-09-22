class LimpError(Exception):
    pass


class UndefinedSymbol(LimpError):
    def __init__(self, name):
        message = f"The symbol '{name}' cannot be found in the current context.\n"
        message += "* Has it been defined?\n"
        message += "* Is there a typo?\n"
        message += "* Was it defined with a typo?\n"
        super().__init__(message)

        
class EmptyCode(LimpError):
    def __init__(self):
        super().__init__("There is no code here to run.")


class ExtraClosingParenthesis(LimpError):
    def __init__(self, amount):
        super().__init__(_parentheses_message(amount, "many"))


class MissingClosingParenthesis(LimpError):
    def __init__(self, amount):
        super().__init__(_parentheses_message(amount, "few"))



def _parentheses_message(amount, quantifier):
    message = "There {} {} too {} closing parentheses."
    if amount == 1:
        message = message.format("is", amount, quantifier)
    else:
        message = message.format("are", amount, quantifier)
