import tests.helpers as Helpers
from limp.standard_library.math import *
from tests.syntax import *


RETURN_INPUT = function(['n'], 'n')
CUSTOM_ADD = function(['a', 'b'], invoke(ADD, 'a', 'b'))


def test_invoking_anonymous_functions():
    Helpers.run_evaluation_test_on([
        (invoke(function([], integer(0))),            0),
        (invoke(function([], integer(4))),            4),
        (invoke(RETURN_INPUT, integer(0)),            0),
        (invoke(RETURN_INPUT, integer(9)),            9),
        (invoke(CUSTOM_ADD, integer(10), integer(5)), 15),
        (invoke(CUSTOM_ADD, integer(20), integer(0)), 20),
    ])


def test_invoking_shorthand_zero_argument_functions():
    Helpers.run_evaluation_test_on([
        (invoke(shorthand_function(integer(1))), 1),
        (invoke(shorthand_function(integer(2))), 2),
    ])
        
