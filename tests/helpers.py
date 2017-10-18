import limp
import limp.environment as Environment
import operator
from nose.tools import assert_equal


ARBITRARY_NAME = "arbitrary"
ARBITRARY_VALUES = [0, 1, "value"]
ARBITRARY_LIMP_FUNCTION = f"(function ({ARBITRARY_NAME}) {ARBITRARY_NAME})"
ARBITRARY_PYTHON_FUNCTION = lambda x: x


def sample_environment():
    environment = Environment.create_standard()
    extras = {
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
    environment.define_batch_of(extras)
    return environment


def assert_form_evaluates_to(expected_value, contents, _type):
    value = _type(contents, sample_environment()).evaluate()
    return assert_equal, expected_value, value


def run_evaluation_test_on(data):
    for source_code, expected_result in data:
        assert_equal(expected_result, limp.evaluate(source_code))
