import inspect
import limp.errors as Errors
from nose.tools import assert_true


PARENT_EXCEPTION = Errors.LimpError


def test_all_exceptions_inherit_from_custom_parent():
    exceptions = _all_exceptions_in(Errors)
    for exception in exceptions:
        yield assert_true, issubclass(exception, PARENT_EXCEPTION)


def _all_exceptions_in(module):
    contents = [getattr(module, thing) for thing in dir(module)]
    classes = [thing for thing in contents if inspect.isclass(thing)]
    exceptions = [thing for thing in classes if issubclass(thing, Exception)]
    return exceptions

