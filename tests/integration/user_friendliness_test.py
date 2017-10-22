import functools
import limp
import limp.environment as Environment
import tests.helpers as Helpers
from nose.tools import assert_equals, assert_raises
from tests.syntax import *
from limp.standard_library import *
from limp.standard_library.math import *


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


def test_that_clean_environment_is_created_automatically():
    VARIABLE = symbol('foo')
    _EVALUATE(define(VARIABLE, integer(10)))
    access_undefined_symbol = functools.partial(_EVALUATE, VARIABLE)
    yield assert_raises, Exception, access_undefined_symbol

        
def test_that_environment_can_be_provided():
    data = [
        (define(symbol('x'), integer(10)), symbol('x'), 10),
        (define(symbol('y'), integer(20)), symbol('y'), 20),
        (define(symbol('z'), integer(30)), symbol('z'), 30),
    ]
    environment = Environment.create_empty()
    run = lambda source_code: _EVALUATE(source_code, environment)
    for definition_code, access_code, expected_result in data:
        run(definition_code)
        result = run(access_code)
        yield assert_equals, expected_result, result
