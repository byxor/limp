from limp.errors import *
from nose.tools import assert_true


def test_all_exceptions_inherit_from_custom_parent():
    expected_parent = LimpError
    data = [
        UndefinedSymbol,
        RedefinedSymbol,
        EmptyCode,
        ExtraClosingParenthesis,
        MissingClosingParenthesis,
        UnnecessarySequentialEvaluator,
        UnclosedString,
        EmptyInvocation,
    ]
    for exception in data:
        yield assert_true, issubclass(exception, expected_parent)
