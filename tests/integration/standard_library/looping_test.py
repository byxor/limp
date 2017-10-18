import limp
import limp.environment as Environment
from nose.tools import assert_equal
from unittest.mock import MagicMock


FUNCTION_NAME = 'my_function'
ARBITRARY_ITERATION_LIMIT = 100


def test_executing_something_a_fixed_number_of_times():
    for iterations in range(ARBITRARY_ITERATION_LIMIT):
        my_function = MagicMock()
        environment = Environment.create_standard()
        environment.define(FUNCTION_NAME, my_function)
        limp.evaluate(f'(times {iterations} {FUNCTION_NAME})', environment)
        yield (assert_equal, iterations, my_function.call_count)


def test_iterating_a_fixed_number_of_times():
    my_function = MagicMock()
    environment = Environment.create_standard()
    environment.define(FUNCTION_NAME, my_function)
    limp.evaluate(f'(iterate {ARBITRARY_ITERATION_LIMIT} {FUNCTION_NAME})', environment)
    for i in range(ARBITRARY_ITERATION_LIMIT):
        yield (my_function.assert_any_call, i)
