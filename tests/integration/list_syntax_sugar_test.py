import tests.helpers as Helpers
from tests.syntax import *


def test():
    Helpers.run_evaluation_test_on([
        (shorthand_list_of(),                             []),
        (shorthand_list_of(integer(1)),                   [1]),
        (shorthand_list_of(float_(0.1), float_(0.2)),     [0.1, 0.2]),
        (shorthand_list_of(string("foo"), string("bar")), ["foo", "bar"]),
    ])
