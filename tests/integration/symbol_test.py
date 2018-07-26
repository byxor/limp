import limp
import limp.errors as Errors
import tests.helpers as Helpers
from nose.tools import assert_raises
from tests.syntax import *


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
