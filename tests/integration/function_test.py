import tests.helpers as Helpers
from limp.standard_library.math import *
from limp.standard_library.comparisons import *
from tests.syntax import *


SQUARE_ROOT = function(['n'], invoke(SQUARE_ROOT, 'n'))
SUBTRACT = function(['a', 'b'], invoke(SUBTRACT, 'a', 'b'))
SELF_REFERENCING_FUNCTION = function(
    ['n'],
    conditional(
        (invoke(GREATER_THAN, 'n', integer(0)),
         invoke(ADD, integer(1), invoke(self_reference(), invoke(SUBTRACT, 'n', integer(1))))),

        (boolean(True),
         integer(0))
    )
)


t0 = Helpers.evaluation_fixture("test_invoking_anonymous_functions", [
    (invoke(function([], integer(10))),        10),
    (invoke(function([], integer(20))),        20),
    (invoke(SQUARE_ROOT, integer(16)),         4),
    (invoke(SQUARE_ROOT, integer(9)),          3),
    (invoke(SUBTRACT, integer(5), integer(3)), 2),
])


t1 = Helpers.evaluation_fixture("test_self_referencing_functions", [
    (invoke(SELF_REFERENCING_FUNCTION, integer(0)), 0),
    (invoke(SELF_REFERENCING_FUNCTION, integer(1)), 1),
    (invoke(SELF_REFERENCING_FUNCTION, integer(2)), 2),
])
