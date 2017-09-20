class UndefinedSymbol(Exception):
    def __init__(self, name):
        super().__init__(f"The symbol '{name}' cannot be found in the current context. Has it been defined?")
        
class EmptyCode(Exception):
    def __init__(self):
        super().__init__("There is no code here to run.")
