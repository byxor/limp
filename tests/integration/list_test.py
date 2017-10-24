import tests.helpers as Helpers
from tests.syntax import *


def test():
    Helpers.run_evaluation_test_on([
        (list_of(integer(1), integer(2), integer(3)), [1, 2, 3]),
        (list_of(string("celery"), string("man")),    ["celery", "man"]),
    ])


def test_syntax_sugar():
    Helpers.run_evaluation_test_on([
        (shorthand_list_of(),                             []),
        (shorthand_list_of(integer(1)),                   [1]),
        (shorthand_list_of(float_(0.1), float_(0.2)),     [0.1, 0.2]),
        (shorthand_list_of(string("foo"), string("bar")), ["foo", "bar"]),
    ])
