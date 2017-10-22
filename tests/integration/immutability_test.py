import limp
import limp.environment as Environment
from nose.tools import assert_equal
from tests.syntax import *
from limp.standard_library import *


TEMPORARY_MAP_FUNCTION = function(['n'], invoke('+', 'n', integer(1)))
TEMPORARY_FILTER_FUNCTION = function(['x'], invoke('=', 'x', integer(1)))
TEMPORARY_REDUCE_FUNCTION = function(['a', 'b'], invoke('+', 'a', 'b'))


def test_lists_are_immutable():
    LIST = 'my-list'
    LIST_VALUE = [1, 2, 3]

    environment = Environment.create_standard()
    environment.define(LIST, LIST_VALUE)

    invocations = [
        invoke(LIST_APPEND_ELEMENT, LIST, integer(1)),
        invoke(LIST_CONCATENATE, LIST, list_of(string("foo"), string("bar"))),
        invoke(LIST_MAP, TEMPORARY_MAP_FUNCTION, LIST),
        invoke(LIST_FILTER, TEMPORARY_FILTER_FUNCTION, LIST),
        invoke(LIST_REDUCE, TEMPORARY_REDUCE_FUNCTION, LIST),
        invoke(LIST_FIRST_ELEMENT, LIST),
        invoke(LIST_LAST_ELEMENT, LIST),
        invoke(LIST_ALL_BUT_FIRST, LIST),
        invoke(LIST_ALL_BUT_LAST, LIST),
        invoke(LIST_PREPEND_ELEMENT, LIST, string("foo")),
    ]
    for invocation in invocations:
        print('\nAbout to run...')
        print(invocation)
        print(environment.resolve(LIST))
        limp.evaluate(invocation, environment)

    yield assert_equal, LIST_VALUE, environment.resolve(LIST)
