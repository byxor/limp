import limp
import limp.environment as Environment
import operator
from nose.tools import assert_equals


def evaluation_fixture(name, data):
    def the_test():
        for source_code, expected_result in data:
            print("--------------------------")
            print(source_code)
            result = limp.evaluate(source_code)
            yield assert_equals, expected_result, result
    the_test.__name__ = name
    return the_test


def test_chain(*functions):
    EMPTY_STATE = dict()
    return _chain(EMPTY_STATE, *functions)


def _chain(input_, *functions):
    lastOutput = input_
    for function in functions:
        lastOutput = function(lastOutput)
    return lastOutput
