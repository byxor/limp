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
        return self.__has_valid_prefix() and evaluates_safely(self)

    def __has_valid_prefix(self):
        for prefix in self.__valid_prefices():
            if self.__contents.startswith(prefix):
                return True
        return False

    def __valid_prefices(self):
        return set([
            f"{self.__prefix}",
            f"{self.__class__.POSITIVE}{self.__prefix}",
            f"{self.__class__.NEGATIVE}{self.__prefix}"
        ])


def _create_abstract_integer(prefix, base):
    class Type(AbstractInteger):
        PREFIX = prefix
        def __init__(self, contents, environment):
            super().__init__(contents, prefix, base)
    return Type


Integer =     _create_abstract_integer('', 10)
Hexadecimal = _create_abstract_integer('0x', 16)
Binary =      _create_abstract_integer('0b', 2)
Octal =       _create_abstract_integer('0o', 8)


class Float(Form.Constructor,
            Form.EvaluatesSafelyValidityChecker):

    def evaluate(self):
        return float(self._contents)
