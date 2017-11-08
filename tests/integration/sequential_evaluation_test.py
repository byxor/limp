import limp
import limp.errors as Errors
import tests.helpers as Helpers
from limp.standard_library.math import *
from tests.syntax import *
from nose.tools import assert_equal, assert_raises


def test_sequential_evaluators():
    environment = Helpers.sample_environment()

    source_code = sequence(
        define('one', integer(1)),
        define('two', integer(2)),
        define('three', integer(3)),
    )

    limp.evaluate(source_code, environment)

    data = [
        ('one',   1),
        ('two',   2),
        ('three', 3),
    ]
    for symbol, expected_value in data:
        value = environment.resolve(symbol)
        yield assert_equal, expected_value, value


def test_sequential_evaluators_raise_an_error_when_not_needed():
    data = [
        integer(0),
        invoke(ADD, integer(1), integer(2)),
        string('foo'),
    ]
    for source_code in data:
        yield (assert_raises,
               Errors.UnnecessarySequentialEvaluator,
               limp.evaluate, sequence(source_code))


def test_sequential_evaluators_return_value_of_last_form():
    Helpers.run_evaluation_test_on([
        (sequence(integer(1), integer(2), integer(3)), 3),
        (sequence(integer(4), integer(5), integer(6)), 6),
        (sequence(integer(7), string("tayne")),        "tayne"),
    ])
