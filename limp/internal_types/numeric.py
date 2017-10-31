from limp.utils import evaluates_safely


class AbstractInteger:

    POSITIVE = '+'
    NEGATIVE = '-'

    def __init__(self, contents, prefix, base):
        self.__contents = contents
        self.__prefix = prefix
        self.__base = base

    def evaluate(self):
        return int(self.__contents, self.__base)

    def is_valid(self):
        return self.__has_correct_prefix() and evaluates_safely(self)

    def __has_correct_prefix(self):
        correct_prefixes = [
            self.__prefix,
            f"{AbstractInteger.POSITIVE}{self.__prefix}",
            f"{AbstractInteger.NEGATIVE}{self.__prefix}",
        ]
        for correct_prefix in correct_prefixes:
            if self.__contents.startswith(correct_prefix):
                return True
        return False



class Integer(AbstractInteger):
    def __init__(self, contents, environment):
        super().__init__(contents, '', 10)


class Hexadecimal(AbstractInteger):
    def __init__(self, contents, environment):
        super().__init__(contents, '0x', 16)


class Binary(AbstractInteger):
    def __init__(self, contents, environment):
        super().__init__(contents, '0b', 2)


class Octal(AbstractInteger):
    def __init__(self, contents, environment):
        super().__init__(contents, '0o', 8)


class Float:

    def __init__(self, contents, environment):
        self.__contents = contents

    def evaluate(self):
        return float(self.__contents)

    def is_valid(self):
        return evaluates_safely(self)
