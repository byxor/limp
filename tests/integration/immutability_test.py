import limp
import limp.environment as Environment
from nose.tools import assert_equal
from tests.syntax import *


MAP_FUNCTION = function(['n'], invoke('+', 'n', integer(1)))
FILTER_FUNCTION = function(['x'], invoke('=', 'x', integer(1)))
REDUCE_FUNCTION = function(['a', 'b'], invoke('+', 'a', 'b'))


def test_lists_are_immutable():
    LIST = 'my-list'
    LIST_VALUE = [1, 2, 3]

    environment = Environment.create_standard()
    environment.define(LIST, LIST_VALUE)

    invocations = [
        invoke('append', LIST, integer(1)),
        invoke('concatenate', LIST, list_of(string("foo"), string("bar"))),
        invoke('map', MAP_FUNCTION, LIST),
        invoke('filter', FILTER_FUNCTION, LIST),
        invoke('reduce', REDUCE_FUNCTION, LIST),
        invoke('first', LIST),
        invoke('last', LIST),
        invoke('all-but-first', LIST),
        invoke('all-but-last', LIST),
        invoke('prepend', LIST, string("foo")),
    ]
    for invocation in invocations:
        print('\nAbout to run...')
        print(invocation)
        print(environment.resolve(LIST))
        limp.evaluate(invocation, environment)

    yield assert_equal, LIST_VALUE, environment.resolve(LIST)
