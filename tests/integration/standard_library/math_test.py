import tests.helpers as Helpers
from tests.syntax import *
from tests.standard_library import *


def test():
    Helpers.run_evaluation_test_on([
        (invoke(ADD, integer(1), integer(1)),             2),
        (invoke(ADD, integer(2), integer(3)),             5),
        (invoke(ADD, integer(1), integer(2), integer(3)), 6),
        
        (invoke(SUBTRACT, integer(1), integer(1)),             0),
        (invoke(SUBTRACT, integer(4), integer(2)),             2),
        (invoke(SUBTRACT, integer(9), integer(8), integer(7)), -6),

        (invoke(MULTIPLY, integer(2), integer(3)),             6),
        (invoke(MULTIPLY, integer(4), integer(1)),             4),
        (invoke(MULTIPLY, integer(2), integer(3), integer(4)), 24),

        (invoke(DIVIDE, integer(4), integer(2)),             2),
        (invoke(DIVIDE, integer(1), integer(2)),             0.5),
        (invoke(DIVIDE, integer(1), integer(2), integer(3)), ((1 / 2) / 3)),

        (invoke(INTEGER_DIVIDE, integer(1), integer(2)),              0),
        (invoke(INTEGER_DIVIDE, integer(5), integer(2)),              2),
        (invoke(INTEGER_DIVIDE, integer(99), integer(2), integer(2)), ((99 // 2) // 2)),

        (invoke(EXPONENT, integer(2), integer(3)), 8),
        (invoke(EXPONENT, integer(0), integer(0)), 1),

        (invoke(SQUARE_ROOT, integer(144)), 12),
        (invoke(SQUARE_ROOT, integer(0)),   0),
        (invoke(SQUARE_ROOT, integer(1)),   1),

        (invoke(FACTORIAL, integer(0)), 1),
        (invoke(FACTORIAL, integer(1)), 1),
        (invoke(FACTORIAL, integer(4)), 24),
        (invoke(FACTORIAL, integer(7)), 5040),

        (invoke(MODULO, integer(4), integer(4)), 0),
        (invoke(MODULO, integer(5), integer(6)), 5),
        (invoke(MODULO, integer(3), integer(1)), 0),

        (invoke(IS_DIVISOR, integer(3), integer(9)),   True),
        (invoke(IS_DIVISOR, integer(3), integer(99)),  True),
        (invoke(IS_DIVISOR, integer(2), integer(44)),  True),
        (invoke(IS_DIVISOR, integer(2), integer(45)),  False),
        (invoke(IS_DIVISOR, integer(44), integer(45)), False),

        (invoke(IS_EVEN, integer(0)), True),
        (invoke(IS_EVEN, integer(1)), False),
        (invoke(IS_EVEN, integer(2)), True),
        (invoke(IS_EVEN, integer(3)), False),
        (invoke(IS_EVEN, integer(4)), True),
        (invoke(IS_EVEN, integer(5)), False),

        (invoke(IS_ODD, integer(0)), False),
        (invoke(IS_ODD, integer(1)), True),
        (invoke(IS_ODD, integer(2)), False),
        (invoke(IS_ODD, integer(3)), True),
        (invoke(IS_ODD, integer(4)), False),
        (invoke(IS_ODD, integer(5)), True),
    ])
