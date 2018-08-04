import limp
import limp.environment as Environment
import operator
from nose.tools import assert_equals


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
    environment.define_multiple(extras.items())
    return environment


def evaluation_fixture(name, data):
    def the_test():
        for source_code, expected_result in data:
            print("--------------------------")
            print(source_code)
            result = limp.evaluate(source_code)
            yield assert_equals, expected_result, result
    the_test.__name__ = name
    return the_test


def run_evaluation_test_with_sample_environment(data):
    for source_code, expected_result in data:
        assert_equals(expected_result, limp.evaluate(source_code, sample_environment()))


def test_chain(*functions):
    EMPTY_STATE = dict()
    return _chain(EMPTY_STATE, *functions)


def _chain(input_, *functions):
    lastOutput = input_
    for function in functions:
        lastOutput = function(lastOutput)
    return lastOutput
