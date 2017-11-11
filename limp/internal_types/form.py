from limp.utils import *


class Constructor:

    def __init__(self, contents, environment):
        self._contents = contents
        self._environment = environment


class EvaluatesSafelyValidityChecker:

    def is_valid(self):
        return evaluates_safely(self)


def create_keyword_validity_checker(expected_index=0):

    class KeywordValidityChecker:

        def is_valid(self):
            if self.__has_enough_contents():
                return self._contents[expected_index] == self.__class__.KEYWORD
            else:
                return False

        def __has_enough_contents(self):
            if expected_index >= 0:
                minimum_required_length = expected_index + 1
            else:
                minimum_required_length = (-1) * expected_index
            return len(self._contents) >= minimum_required_length

    return KeywordValidityChecker
