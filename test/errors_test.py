import functools
import limp
import limp.errors as Errors
from nose.tools import assert_raises


def test_exception_raised_when_accessing_non_existent_variable():
    accessing_non_existent_variable = functools.partial(limp.evaluate, 'year')
    yield assert_raises, Errors.UndefinedSymbol, accessing_non_existent_variable
