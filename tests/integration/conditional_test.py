import tests.helpers as Helpers
from limp.standard_library.comparisons import *
from tests.syntax import *


t0 = Helpers.evaluation_fixture("test_conditionals", [
    (conditional((boolean(True), string("yes"))),                                  "yes"),
    (conditional((boolean(True), string("aye")), (boolean(True), string("no"))),   "aye"),
    (conditional((boolean(False), string("aye")), (boolean(True), string("no"))),  "no"),
    (conditional((boolean(False), string("aye")), (boolean(True), string("nah"))), "nah"),

    (conditional(
        (invoke(GREATER_THAN, integer(0), integer(10)), string("Are you dumb?")),
        (boolean(True), string("You smart."))),
     "You smart."),

    (conditional((boolean(True), integer(0))), 0),

    (conditional((boolean(True), integer(1))), 1),

    (conditional(
        (boolean(False), integer(0)),
        (boolean(True),  integer(1))),
     1),

    (conditional(
        (invoke(ARE_EQUAL, integer(0), integer(1)), string("NotThisOne")),
        (invoke(ARE_EQUAL, integer(0), integer(2)), string("NorThisOne")),
        (invoke(ARE_EQUAL, integer(0), integer(0)), string("This one!")),
        (invoke(ARE_EQUAL, integer(0), integer(3)), string("NorNorThisOne"))),
     "This one!"),
])


t1 = Helpers.evaluation_fixture("test_default_return_values", [
    (conditional(
        (boolean(False), string("nope")),
        string("default")),
     "default"),

    (conditional(
        (invoke(ARE_EQUAL, integer(0), integer(1)), string("NotThisOne")),
        (invoke(ARE_EQUAL, integer(0), integer(2)), string("NorThisOne")),
        (invoke(ARE_EQUAL, integer(0), integer(3)), string("This one!")),
        (invoke(ARE_EQUAL, integer(0), integer(4)), string("NorNorThisOne")),
        (integer(10))),
     10),
])


t2 = Helpers.evaluation_fixture("test_nested_conditionals", [
    (conditional(
        (boolean(False),
         string("NotMe!")),
        (boolean(True),
         conditional(
             (boolean(False),
              string("IT ISN'T ME")),
             string("Bingo")
         ))
    ), "Bingo"),
])
