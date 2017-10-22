import tests.helpers as Helpers
from tests.syntax import *
from limp.standard_library import *


def test_integer_comparison():
    Helpers.run_evaluation_test_on([
        (invoke(GREATER_THAN, integer(1), integer(0)),      True),
        (invoke(GREATER_THAN, integer(1), integer(1)),      False),
        (invoke(GREATER_THAN, integer(9999), integer(321)), True),
        (invoke(GREATER_THAN, integer(-10), integer(-20)),  True),

        (invoke(LESS_THAN, integer(10), integer(11)),    True),
        (invoke(LESS_THAN, integer(11), integer(11)),    False),
        (invoke(LESS_THAN, integer(12), integer(10)),    False),
        (invoke(LESS_THAN, integer(100), integer(4321)), True),
        (invoke(LESS_THAN, integer(-99), integer(-12)),  True),

        (invoke(GREATER_THAN_OR_EQUAL, integer(1), integer(0)),      True),
        (invoke(GREATER_THAN_OR_EQUAL, integer(1), integer(1)),      True),
        (invoke(GREATER_THAN_OR_EQUAL, integer(0), integer(1)),      False),
        (invoke(GREATER_THAN_OR_EQUAL, integer(9999), integer(321)), True),
        (invoke(GREATER_THAN_OR_EQUAL, integer(-10), integer(-20)), True),

        (invoke(LESS_THAN_OR_EQUAL, integer(10), integer(11)),    True),
        (invoke(LESS_THAN_OR_EQUAL, integer(11), integer(11)),    True),
        (invoke(LESS_THAN_OR_EQUAL, integer(12), integer(10)),    False),
        (invoke(LESS_THAN_OR_EQUAL, integer(100), integer(4321)), True),
        (invoke(LESS_THAN_OR_EQUAL, integer(-99), integer(-12)),  True),
    ])
