class Constructor:
    def __init__(self, contents, environment):
        self._contents = contents
        self._environment = environment


class KeywordValidityChecker:
    def is_valid(self):
        return self._contents[0] == self.__class__.KEYWORD
