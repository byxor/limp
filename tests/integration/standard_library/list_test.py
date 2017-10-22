import tests.helpers as Helpers
from tests.syntax import *
from limp.standard_library import *


VARIABLE = "variable"
NUMBERS =  list_of(integer(1), integer(2), integer(3), integer(4))
STRINGS =  list_of(string("foo"), string("bar"), string("baz"))
EMPTY =    list_of()


def test():
    Helpers.run_evaluation_test_on([ 

        (invoke(LIST_MAP, function([VARIABLE], invoke(MULTIPLY, VARIABLE, integer(2))), NUMBERS),
         [2, 4, 6, 8]),

        (invoke(LIST_MAP, function([VARIABLE], invoke(ADD, VARIABLE, integer(1))), NUMBERS),
         [2, 3, 4, 5]),
        
        (invoke(LIST_MAP, function([VARIABLE], invoke(DIVIDE, VARIABLE, integer(2))), list_of(integer(10), integer(20))),
         [5, 10]),
        
        (invoke(LIST_FILTER, function([VARIABLE], invoke(ARE_EQUAL, invoke(MODULO, VARIABLE, integer(2)), integer(0))), NUMBERS),
         [2, 4]),

        (invoke(LIST_FILTER, function([VARIABLE], invoke(ARE_EQUAL, invoke(MODULO, VARIABLE, integer(2)), integer(1))), NUMBERS),
         [1, 3]),

        (invoke(LIST_FILTER, function([VARIABLE], invoke(ARE_EQUAL, VARIABLE, integer(1))), NUMBERS),
         [1]),

        (invoke(LIST_REDUCE, ADD, NUMBERS), 10),
        (invoke(LIST_REDUCE, SUBTRACT, NUMBERS), -8),

        (invoke(LIST_GET_ELEMENT, NUMBERS, integer(0)), 1),
        (invoke(LIST_GET_ELEMENT, NUMBERS, integer(1)), 2),
        (invoke(LIST_GET_ELEMENT, NUMBERS, integer(2)), 3),
        (invoke(LIST_GET_ELEMENT, NUMBERS, integer(3)), 4),
        (invoke(LIST_GET_ELEMENT, STRINGS, integer(0)), "foo"),
        (invoke(LIST_GET_ELEMENT, STRINGS, integer(1)), "bar"),
        (invoke(LIST_GET_ELEMENT, STRINGS, integer(2)), "baz"),

        (invoke(LIST_APPEND_ELEMENT, EMPTY, integer(1)),      [1]),
        (invoke(LIST_APPEND_ELEMENT, STRINGS, string("qux")), ["foo", "bar", "baz", "qux"]),
        (invoke(LIST_APPEND_ELEMENT, NUMBERS, integer(5)),    [1, 2, 3, 4, 5]),

        (invoke(LIST_PREPEND_ELEMENT, EMPTY, integer(1)),     [1]),
        (invoke(LIST_PREPEND_ELEMENT, STRINGS, string("hi")), ["hi", "foo", "bar", "baz"]),
        (invoke(LIST_PREPEND_ELEMENT, NUMBERS, integer(0)),   [0, 1, 2, 3, 4]),

        (invoke(LIST_CONCATENATE, NUMBERS, NUMBERS),                            [1, 2, 3, 4, 1, 2, 3, 4]),
        (invoke(LIST_CONCATENATE, NUMBERS, integer(0), integer(0), integer(1)), [1, 2, 3, 4, 0, 0, 1]),
        
        (invoke(LIST_FIRST_ELEMENT, NUMBERS), 1),
        (invoke(LIST_FIRST_ELEMENT, STRINGS), "foo"),

        (invoke(LIST_LAST_ELEMENT, NUMBERS), 4),
        (invoke(LIST_LAST_ELEMENT, STRINGS), "baz"),

        (invoke(LIST_ALL_BUT_FIRST, NUMBERS), [2, 3, 4]),
        (invoke(LIST_ALL_BUT_FIRST, STRINGS), ["bar", "baz"]),

        (invoke(LIST_ALL_BUT_LAST, NUMBERS), [1, 2, 3]),
        (invoke(LIST_ALL_BUT_LAST, STRINGS), ["foo", "bar"]),

        (invoke(LIST_LENGTH, NUMBERS), 4),
        (invoke(LIST_LENGTH, STRINGS), 3),

        (invoke(LIST_CONTAINS, NUMBERS, integer(1)),  True),
        (invoke(LIST_CONTAINS, NUMBERS, integer(2)),  True),
        (invoke(LIST_CONTAINS, NUMBERS, integer(3)),  True),
        (invoke(LIST_CONTAINS, NUMBERS, integer(4)),  True),
        (invoke(LIST_CONTAINS, NUMBERS, integer(5)),  False),
    ])

