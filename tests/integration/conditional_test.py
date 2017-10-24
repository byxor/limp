import tests.helpers as Helpers
from limp.standard_library.comparisons import *
from tests.syntax import *


def test_simple_conditional_statements():
    Helpers.run_evaluation_test_on([
        (if_statement(boolean(True), string("yes")),                 "yes"),
        (if_statement(boolean(True), string("aye"), string("no")),   "aye"),
        (if_statement(boolean(False), string("aye"), string("no")),  "no"),
        (if_statement(boolean(False), string("aye"), string("nah")), "nah"),

        (if_statement(
            invoke(GREATER_THAN, integer(10), integer(0)),
            string("You know it")),
         "You know it"),

        (if_statement(
            invoke(GREATER_THAN, integer(0), integer(10)),
            string("Are you dumb?"),
            string("You smart.")),
         "You smart."),
    ])


def test_complex_conditional_statements():
    Helpers.run_evaluation_test_on([
        (conditional([boolean(True), integer(0)]), 0),
        (conditional([boolean(True), integer(1)]), 1),

        (conditional(
            [boolean(False), integer(0)],
            [boolean(True), integer(1)]),
         1),

        (conditional(
            [invoke(ARE_EQUAL, integer(0), integer(1)), string("NotThisOne")],
            [invoke(ARE_EQUAL, integer(0), integer(2)), string("NorThisOne")],
            [invoke(ARE_EQUAL, integer(0), integer(0)), string("This one!")],
            [invoke(ARE_EQUAL, integer(0), integer(3)), string("NorNorThisOne")]),
         "This one!")
    ])