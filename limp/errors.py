class LimpError(Exception):
    pass


class UndefinedSymbol(LimpError):
    def __init__(self, name):
        message = "The symbol..."
        message += f"\n'{name}' cannot be found in the current context.\n"
        message += "* Has it been defined?\n"
        message += "* Is there a typo?\n"
        message += "* Was it defined with a typo?"
        super().__init__(message)


class RedefinedSymbol(LimpError):
    def __init__(self, name):
        message = f"The symbol '{name}' already exists, you can't redefine it.\n"
        message += "It may seem annoying, but immutability has benefits."
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


class EmptyInvocation(LimpError):
    def __init__(self):
        message = "You cannot invoke nothing.\n\n"
        message += "* Wrapping a function in parentheses will invoke it.\n"
        message += "* Did you write '()' by mistake?"
        super().__init__(message)


def _parentheses_message(amount, quantifier):
    message = "There {} {} too {} closing parentheses."
    if amount == 1:
        message = message.format("is", amount, quantifier)
    else:
        message = message.format("are", amount, quantifier)
    return message


class UnclosedString(LimpError):
    def __init__(self):
        message = "You forgot to close a string literal."
        super().__init__(message)
