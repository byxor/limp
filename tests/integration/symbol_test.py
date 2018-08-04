import limp
import limp.errors as Errors
import limp.environment as Environment
import tests.helpers as Helpers
import operator
from nose.tools import *
from tests.syntax import *



def test_getting_symbols():
    symbols = {
        'variable': 20,
        'abc': None,
        'def': None,
        'add': operator.add,
        'subtract': operator.sub,
        'multiply': lambda x, y, z: x * y * z,
        'return10': lambda: 10,
        'x': 10,
        'y': 20,
        'z': 30,
        'foo': 100,
    }

    environment = Environment.create_standard()
    environment.define_multiple(symbols.items())

    data = [
        ('x',   10),
        ('y',   20),
        ('z',   30),
        ('foo', 100),
    ]

    for source_code, expected_result in data:
        result = limp.evaluate(source_code, environment)
        yield assert_equal, expected_result, result


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
        yield assert_raises, Errors.UndefinedSymbol, limp.evaluate, source_code
