import limp
from nose.tools import assert_equal
from tests.syntax import *


# It's easy for string literals to be
# unintentionally modified when
# interpreting source code.

# These tests will reduce that.


def test_ascii_literals_remain_unmodified():
    LOWEST_ORDINAL = 32
    HIGHEST_ORDINAL = 126
    ORDINALS = lambda: range(LOWEST_ORDINAL, HIGHEST_ORDINAL + 1)

    EXCLUSIONS = [
        Types.String.DELIMITER
    ]

    for ordinal in ORDINALS():
        character = chr(ordinal)
        if not character in EXCLUSIONS:
            source_code = string(character)
            yield assert_equal, character, limp.evaluate(source_code)


def test_miscellaneous_strings_remain_unmodified():
    data = [
        "[]",
        "()",
        "[ ]",
    ]
    for string_ in data:
        source_code = string(string_)
        yield assert_equal, string_, limp.evaluate(source_code)
