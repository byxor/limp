import limp
import limp.environment as Environment
import limp.errors as Errors
import tests.helpers as Helpers
from nose.tools import assert_equal, assert_raises
from tests.syntax import *
from functools import partial


def test_accessing_symbols():
    Helpers.run_evaluation_test_with_sample_environment([
        ('x',   10),
        ('y',   20),
        ('z',   30),
        ('foo', 100),
    ])

        
def test_exception_raised_when_accessing_non_existent_symbols():
    data = [
        'year',
        'boy',
        'bones',
        'dyliams',
        'antichav',
        'sesh'
    ]
    for source_code in data:
        yield assert_raises, Errors.LimpError, limp.evaluate, source_code


def test_defining_symbols():
    data = [
        ('age', integer(20), 20),
        ('abc', integer(52), 52),
    ]
    for name, value, expected_value in data:
        environment = Environment.create_empty()
        source_code = define(name, value)
        limp.evaluate(source_code, environment)
        value = limp.evaluate(name, environment)
        yield assert_equal, expected_value, value


def test_redefining_symbols_raises_an_exception():
    data = ['foo', 'bar', 'baz']
    for name in data:
        environment = Environment.create_empty()
        value = string("does not matter")
        source_code = define(name, value)
        define_symbol = partial(limp.evaluate, source_code, environment)
        define_symbol()
        yield assert_raises, Errors.RedefinedSymbol, define_symbol
