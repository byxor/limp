import limp.syntax as Syntax


class LimpError(Exception):
    pass


class UndefinedSymbol(LimpError):
    def __init__(self, name):
        message = "The symbol..."
        message += f"\n'{name}' cannot be found in the current context.\n\n"
        message += "* Has it been defined?\n"
        message += "* Is there a typo?\n"
        message += "* Was it defined with a typo?"
        super().__init__(message)


class RedefinedSymbol(LimpError):
    def __init__(self, name):
        message = f"The symbol '{name}' already exists, you can't redefine it.\n\n"
        message += "It may seem annoying, but immutability has benefits."
        super().__init__(message)


class EmptyCode(LimpError):
    def __init__(self):
        super().__init__("There is no code here to run.")


class EmptyFunctionCall(LimpError):
    def __init__(self):
        message = "You cannot invoke nothing.\n\n"
        message += "* Wrapping a function in parentheses will invoke it.\n"
        message += "* Did you write '()' by mistake?"
        super().__init__(message)


class UnclosedString(LimpError):
    def __init__(self):
        message = "You forgot to close a string literal."
        super().__init__(message)


class MalformedObject(LimpError):
    def __init__(self):
        message = "There's something wrong with one of your object literals."
        super().__init__(message)


class IncorrectObjectDelimiter(LimpError):
    def __init__(self):
        message = f"Object literals require {Syntax.OBJECT_DELIMITER} between keys and values."
        super().__init__(message)
