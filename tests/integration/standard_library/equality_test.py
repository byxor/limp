import tests.helpers as Helpers
import limp
from tests.syntax import *
from limp.standard_library.comparisons import *
from nose.tools import assert_equal


DATA = [
    (integer(9), integer(9), True),
    (integer(1), integer(1), True),
    (integer(1), integer(5), False),

    (string(""), string(""),           True),
    (string("a"), string("a"),         True),
    (string("ab"), string("ab"),       True),
    (string("car"), string("avan"),    False),
    (string("tayne"), string("mayne"), False),

    (boolean(True), boolean(True),   True),
    (boolean(False), boolean(False), True),
    (boolean(True), boolean(False),  False),
    (boolean(False), boolean(True),  False),
]


def test_equality():
    for a, b, expected_equality in DATA:
        source_code = invoke(ARE_EQUAL, a, b)
        yield assert_equal, limp.evaluate(source_code), expected_equality


def test_inequality():
    for a, b, expected_equality in DATA:
        source_code = invoke(ARE_NOT_EQUAL, a, b)
        yield assert_equal, limp.evaluate(source_code), not expected_equality
