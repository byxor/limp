import limp
import limp.environment as Environment
from nose.tools import assert_equal
from unittest.mock import MagicMock
from tests.syntax import *
from tests.standard_library import *


FUNCTION_NAME = 'my_function'
ARBITRARY_ITERATION_LIMIT = 100


def test_executing_something_a_fixed_number_of_times():
    for iterations in range(ARBITRARY_ITERATION_LIMIT):
        my_function = MagicMock()
        environment = Environment.create_standard()
        environment.define(FUNCTION_NAME, my_function)
        code = invoke(TIMES, integer(iterations), symbol(FUNCTION_NAME))
        limp.evaluate(code, environment)
        yield (assert_equal, iterations, my_function.call_count)


def test_iterating_a_fixed_number_of_times():
    my_function = MagicMock()
    environment = Environment.create_standard()
    environment.define(FUNCTION_NAME, my_function)
    code = invoke(ITERATE, integer(ARBITRARY_ITERATION_LIMIT), symbol(FUNCTION_NAME))
    limp.evaluate(code, environment)
    for i in range(ARBITRARY_ITERATION_LIMIT):
        yield (my_function.assert_any_call, i)
