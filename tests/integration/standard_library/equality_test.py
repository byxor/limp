import tests.helpers as Helpers
from tests.syntax import *
from limp.standard_library import *


def test():
    Helpers.run_evaluation_test_on([
        # Integers
        (invoke(ARE_EQUAL, integer(9), integer(9)), True),
        (invoke(ARE_EQUAL, integer(1), integer(5)), False),
        (invoke(ARE_EQUAL, integer(1), integer(1)), True),

        # String
        (invoke(ARE_EQUAL, string(""), string("")),          True),
        (invoke(ARE_EQUAL, string("a"), string("a")),        True),
        (invoke(ARE_EQUAL, string("ab"), string("ab")),      True),
        (invoke(ARE_EQUAL, string("car"), string("avan")),   False),
        (invoke(ARE_EQUAL, string("tayne"), string("mayne")), False),

        # Booleans
        (invoke(ARE_EQUAL, boolean(True), boolean(True)),   True),
        (invoke(ARE_EQUAL, boolean(False), boolean(False)), True),
        (invoke(ARE_EQUAL, boolean(True), boolean(False)),  False),
        (invoke(ARE_EQUAL, boolean(False), boolean(True)),  False),
    ])
