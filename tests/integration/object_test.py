import tests.helpers as Helpers
from tests.syntax import *
from limp.standard_library.objects import *


_NAME = "name"
_AGE = "age"
_X = "x"
_Y = "y"


BOB =      object_([_NAME, string("bob")],  [_AGE, integer(20)])
JANE =     object_([_NAME, string("jane")], [_AGE, integer(56)])
POSITION = object_([_X,    float_(0.0)],    [_Y,   float_(0.5)])


def test_creating_objects():
    Helpers.run_evaluation_test_on([
        (BOB, {
            _NAME: "bob",
            _AGE: 20
        }),

        (JANE, {
            _NAME: "jane",
            _AGE: 56
        }),

        (POSITION, {
            _X: 0.0,
            _Y: 0.5
        }),
    ])


def test_getting_attributes_from_objects():
    Helpers.run_evaluation_test_on([
        (invoke(GET_ATTRIBUTE, BOB, string(_NAME)), "bob"),
        (invoke(GET_ATTRIBUTE, BOB, string(_AGE)),  20),
        
        (invoke(GET_ATTRIBUTE, JANE, string(_NAME)), "jane"),
        (invoke(GET_ATTRIBUTE, JANE, string(_AGE)),  56),

        (invoke(GET_ATTRIBUTE, POSITION, string(_X)), 0.0),
        (invoke(GET_ATTRIBUTE, POSITION, string(_Y)), 0.5),
    ])
