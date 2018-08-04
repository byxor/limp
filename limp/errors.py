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
