import functools
import limp
import test.helpers as Helpers
from nose.tools import assert_equals, assert_raises


_EVALUATE = limp.evaluate


def test_that_code_can_be_evaluated_with_a_simple_import():
    data = [
        ('10',       10),
        ('(- 5 3)',  2),
        ('(* 50 2)', 100),
    ]
    for code, expected_result in data:
        result = _EVALUATE(code)
        yield assert_equals, expected_result, result


def test_that_clean_environment_is_created_automatically():
    _EVALUATE('(define x 10)')
    access_undefined_symbol = functools.partial(_EVALUATE, 'x')
    yield assert_raises, Exception, access_undefined_symbol

        
def test_that_environment_can_be_provided():
    data = [
        ('(define x 10)', 'x', 10),
        ('(define y 20)', 'y', 20),
        ('(define z 30)', 'z', 30),
    ]
    environment = Helpers.SIMPLE_ENVIRONMENT
    run = lambda source_code: _EVALUATE(source_code, environment)
    for definition_code, access_code, expected_result in data:
        run(definition_code)
        result = run(access_code)
        yield assert_equals, expected_result, result
