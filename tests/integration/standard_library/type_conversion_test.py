import tests.helpers as Helpers
from tests.syntax import *
from limp.standard_library.conversions import *


def test():
    Helpers.run_evaluation_test_on([
        (invoke(STRING, integer(123)),  "123"),
        (invoke(STRING, float_(0.1)),   "0.1"),
        (invoke(STRING, boolean(True)), "True"),
        (invoke(STRING, string("foo")), "foo"),

        (invoke(INTEGER, string("32")), 32),
        (invoke(INTEGER, string("-1")), -1),
        (invoke(INTEGER, integer(10)),  10),

        (invoke(FLOAT, string("5.2")), 5.2),
        (invoke(FLOAT, string("0.3")), 0.3),
        (invoke(FLOAT, float_(9.99)),  9.99),

        (invoke(BOOLEAN, string("false")), False),
        (invoke(BOOLEAN, string("true")),  True),
        (invoke(BOOLEAN, integer(1)),      True),
        (invoke(BOOLEAN, integer(0)),      False),
        (invoke(BOOLEAN, boolean(True)),   True),
        (invoke(BOOLEAN, boolean(False)),  False),
    ])
