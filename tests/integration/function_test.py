import tests.helpers as Helpers
from limp.standard_library.math import *
from limp.standard_library.comparisons import *
from tests.syntax import *


RETURN_INPUT = function(['n'], 'n')
CUSTOM_ADD = function(['a', 'b'], invoke(ADD, 'a', 'b'))

SHORTHAND_SQUARE_ROOT = shorthand_function(['n'], invoke(SQUARE_ROOT, 'n'))
SHORTHAND_SUBTRACT = shorthand_function(['a', 'b'], invoke(SUBTRACT, 'a', 'b'))


def test_invoking_anonymous_functions():
    Helpers.run_evaluation_test_on([
        (invoke(function([], integer(0))),            0),
        (invoke(function([], integer(4))),            4),
        (invoke(RETURN_INPUT, integer(0)),            0),
        (invoke(RETURN_INPUT, integer(9)),            9),
        (invoke(CUSTOM_ADD, integer(10), integer(5)), 15),
        (invoke(CUSTOM_ADD, integer(20), integer(0)), 20),
    ])


def test_invoking_shortened_zero_argument_functions():
    Helpers.run_evaluation_test_on([
        (invoke(shortened_function(integer(1))), 1),
        (invoke(shortened_function(integer(2))), 2),
    ])


def test_invoking_shorthand_functions():
    Helpers.run_evaluation_test_on([
        (invoke(shorthand_function([], integer(10))),        10),
        (invoke(shorthand_function([], integer(20))),        20),
        (invoke(SHORTHAND_SQUARE_ROOT, integer(16)),         4),
        (invoke(SHORTHAND_SQUARE_ROOT, integer(9)),          3),
        (invoke(SHORTHAND_SUBTRACT, integer(5), integer(3)), 2),
    ])


def test_self_referencing_functions():
    function_ = shorthand_function(
        ['n'],
        if_statement(
            invoke(
                GREATER_THAN,
                'n',
                integer(0)
            ),
            invoke(
                ADD,
                integer(1),
                invoke(
                    self_reference(),
                    invoke(
                        SUBTRACT,
                        'n',
                        integer(1)
                    )
                )
            ),
            integer(0)
        )
    )

    Helpers.run_evaluation_test_on([
        (invoke(function_, integer(0)), 0),
        (invoke(function_, integer(1)), 1),
        (invoke(function_, integer(2)), 2),
    ])
