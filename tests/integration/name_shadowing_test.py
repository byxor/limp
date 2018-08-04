import limp
import limp.environment as Environment
from nose.tools import assert_equal
from tests.syntax import *


ENVIRONMENT = Environment.create_empty()
EVALUATE = lambda code: limp.evaluate(code, ENVIRONMENT)

ARBITRARY_NAME = "arbitrary"
ARBITRARY_VALUES = [0, 1, "value"]


def test_function_parameters_can_shadow_globally_defined_variables():
    REUSABLE_NAME = ARBITRARY_NAME
    OUTER_VALUE, INNER_VALUE = ARBITRARY_VALUES[:2]

    ENVIRONMENT.define(REUSABLE_NAME, OUTER_VALUE)

    SHADOWING_FUNCTION = function([REUSABLE_NAME], REUSABLE_NAME)
    EVALUATE(invoke(SHADOWING_FUNCTION, string(INNER_VALUE)))

    yield (assert_equal, OUTER_VALUE, EVALUATE(REUSABLE_NAME))
