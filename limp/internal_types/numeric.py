from limp.utils import evaluates_safely


class _AbstractInteger:

    def __init__(self, contents, prefix, base):
        self.__contents = contents
        self.__prefix = prefix
        self.__base = base

    def evaluate(self):
        return int(self.__contents, self.__base)

    def is_valid(self):
        has_correct_prefix = self.__contents.startswith(self.__prefix)
        return has_correct_prefix and evaluates_safely(self)

    
class Integer(_AbstractInteger):
    def __init__(self, contents, environment):
        super().__init__(contents, '', 10)

        
class Hexadecimal(_AbstractInteger):
    def __init__(self, contents, environment):
        super().__init__(contents, '0x', 16)

        
class Binary(_AbstractInteger):
    def __init__(self, contents, environment):
        super().__init__(contents, '0b', 2)

        
class Float:

    def __init__(self, contents, environment):
        self.__contents = contents

    def evaluate(self):
        return float(self.__contents)

    def is_valid(self):
        return evaluates_safely(self)
