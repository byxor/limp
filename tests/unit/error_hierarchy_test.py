import inspect
import limp.errors as Errors
from functional import seq
from nose.tools import assert_true, assert_greater_equal


EXPECTED_PARENT_CLASS = Errors.LimpError
MINIMUM_EXPECTED_ERRORS = 8


def test_all_exceptions_inherit_from_custom_parent():
    errors = _all_limp_errors()
    assert_greater_equal(len(errors), MINIMUM_EXPECTED_ERRORS)
    for error in errors:
        yield assert_true, issubclass(error, EXPECTED_PARENT_CLASS)


def _all_limp_errors():
    module_contents = [x[1] for x in inspect.getmembers(Errors)]
    return list(seq(module_contents)
                  .filter(inspect.isclass)
                  .filter(lambda class_: issubclass(class_, Exception))
                  .filter(lambda class_: class_ != EXPECTED_PARENT_CLASS))
