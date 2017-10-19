import tests.helpers as Helpers
from tests.syntax import *
from tests.standard_library import *


VARIABLE = "variable"
NUMBERS =  list_of(integer(1), integer(2), integer(3), integer(4))
STRINGS =  list_of(string("foo"), string("bar"), string("baz"))
EMPTY =    list_of()


def test():
    Helpers.run_evaluation_test_on([ 

        (invoke(MAP, function([VARIABLE], invoke(MULTIPLY, VARIABLE, integer(2))), NUMBERS),
         [2, 4, 6, 8]),

        (invoke(MAP, function([VARIABLE], invoke(ADD, VARIABLE, integer(1))), NUMBERS),
         [2, 3, 4, 5]),
        
        (invoke(MAP, function([VARIABLE], invoke(DIVIDE, VARIABLE, integer(2))), list_of(integer(10), integer(20))),
         [5, 10]),
        
        (invoke(FILTER, function([VARIABLE], invoke(ARE_EQUAL, invoke(MODULO, VARIABLE, integer(2)), integer(0))), NUMBERS),
         [2, 4]),

        (invoke(FILTER, function([VARIABLE], invoke(ARE_EQUAL, invoke(MODULO, VARIABLE, integer(2)), integer(1))), NUMBERS),
         [1, 3]),

        (invoke(FILTER, function([VARIABLE], invoke(ARE_EQUAL, VARIABLE, integer(1))), NUMBERS),
         [1]),

        (invoke(REDUCE, ADD, NUMBERS), 10),
        (invoke(REDUCE, SUBTRACT, NUMBERS), -8),

        (invoke(GET_ELEMENT, NUMBERS, integer(0)), 1),
        (invoke(GET_ELEMENT, NUMBERS, integer(1)), 2),
        (invoke(GET_ELEMENT, NUMBERS, integer(2)), 3),
        (invoke(GET_ELEMENT, NUMBERS, integer(3)), 4),
        (invoke(GET_ELEMENT, STRINGS, integer(0)), "foo"),
        (invoke(GET_ELEMENT, STRINGS, integer(1)), "bar"),
        (invoke(GET_ELEMENT, STRINGS, integer(2)), "baz"),

        (invoke(APPEND_ELEMENT, EMPTY, integer(1)),      [1]),
        (invoke(APPEND_ELEMENT, STRINGS, string("qux")), ["foo", "bar", "baz", "qux"]),
        (invoke(APPEND_ELEMENT, NUMBERS, integer(5)),    [1, 2, 3, 4, 5]),

        (invoke(PREPEND_ELEMENT, EMPTY, integer(1)),     [1]),
        (invoke(PREPEND_ELEMENT, STRINGS, string("hi")), ["hi", "foo", "bar", "baz"]),
        (invoke(PREPEND_ELEMENT, NUMBERS, integer(0)),   [0, 1, 2, 3, 4]),

        (invoke(CONCATENATE, NUMBERS, NUMBERS),                            [1, 2, 3, 4, 1, 2, 3, 4]),
        (invoke(CONCATENATE, NUMBERS, integer(0), integer(0), integer(1)), [1, 2, 3, 4, 0, 0, 1]),
        
        (invoke(FIRST_ELEMENT, NUMBERS), 1),
        (invoke(FIRST_ELEMENT, STRINGS), "foo"),

        (invoke(LAST_ELEMENT, NUMBERS), 4),
        (invoke(LAST_ELEMENT, STRINGS), "baz"),

        (invoke(ALL_BUT_FIRST, NUMBERS), [2, 3, 4]),
        (invoke(ALL_BUT_FIRST, STRINGS), ["bar", "baz"]),

        (invoke(ALL_BUT_LAST, NUMBERS), [1, 2, 3]),
        (invoke(ALL_BUT_LAST, STRINGS), ["foo", "bar"]),

        (invoke(LENGTH, NUMBERS), 4),
        (invoke(LENGTH, STRINGS), 3),
    ])

