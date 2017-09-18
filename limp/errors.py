class UndefinedSymbol(Exception):
    def __init__(self, name):
        super().__init__(f"The symbol '{name}' cannot be found in the current context. Has it been defined?")
        
