import limp.internal_types.form as Form
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


def _create_abstract_integer(prefix, base):
    class Type(AbstractInteger):
        def __init__(self, contents, environment):
            super().__init__(contents, prefix, base)
    return Type


Integer =     _create_abstract_integer('', 10)
Hexadecimal = _create_abstract_integer('0x', 16)
Binary =      _create_abstract_integer('0b', 2)
Octal =       _create_abstract_integer('0o', 8)


class Float(Form.Constructor):

    def is_valid(self):
        return evaluates_safely(self)

    def evaluate(self):
        return float(self._contents)
