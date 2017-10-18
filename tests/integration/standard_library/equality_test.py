import tests.helpers as Helpers
from tests.syntax import *


EQUAL = "="


def test():
    Helpers.run_evaluation_test_on([
        # Integers
        (invoke(EQUAL, integer(9), integer(9)), True),
        (invoke(EQUAL, integer(1), integer(5)), False),
        (invoke(EQUAL, integer(1), integer(1)), True),

        # String
        (invoke(EQUAL, string(""), string("")),          True),
        (invoke(EQUAL, string("a"), string("a")),        True),
        (invoke(EQUAL, string("ab"), string("ab")),      True),
        (invoke(EQUAL, string("car"), string("avan")),   False),
        (invoke(EQUAL, string("tayne"), string("mayne")), False),

        # Booleans
        (invoke(EQUAL, boolean(True), boolean(True)),   True),
        (invoke(EQUAL, boolean(False), boolean(False)), True),
        (invoke(EQUAL, boolean(True), boolean(False)),  False),
        (invoke(EQUAL, boolean(False), boolean(True)),  False),
    ])
