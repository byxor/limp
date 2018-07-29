import limp
import limp.environment as Environment
from nose.tools import assert_equals, assert_not_equals
from tests.syntax import *
from limp.standard_library import *
from limp.standard_library.math import *
from limp.standard_library.meta import *


_EVALUATE = limp.evaluate


def test_that_code_can_be_evaluated_with_a_simple_import():
    data = [
        (integer(0),                                0),
        (invoke(SUBTRACT, integer(5), integer(3)),  2),
        (invoke(MULTIPLY, integer(50), integer(2)), 100),
    ]
    for code, expected_result in data:
        result = _EVALUATE(code)
        yield assert_equals, expected_result, result


def test_that_environment_can_be_provided():
    data = [
        ('x', 10),
        ('y', 20),
        ('z', 30),
    ]
    environment = Environment.create_empty()
    for symbol, value in data:
        environment.define(symbol, value)

    for symbol, value in data:
        yield assert_equals, value, _EVALUATE(symbol, environment)


def test_that_help_information_is_available():
    result = limp.evaluate(HELP)
    yield assert_not_equals, "", result
