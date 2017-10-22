import tests.helpers as Helpers
from tests.syntax import *
from tests.standard_library import *


def test():
    Helpers.run_evaluation_test_on([

        (invoke(STRING_CONCATENATE, string("foo"), string("bar")),
         "foobar"),
        
        (invoke(STRING_CONCATENATE, string("hello"), string(" "), string("there")),
         "hello there"),

        (invoke(STRING_STRIP, string(" x ")),                "x"),
        (invoke(STRING_STRIP, string(" abc ")),              "abc"),
        (invoke(STRING_STRIP, string(" x \t\n")),            "x"),
        (invoke(STRING_STRIP, string("hello \n\t\n there")), "hello \n\t\n there"),

        (invoke(STRING_LENGTH, string("")),      0),
        (invoke(STRING_LENGTH, string("a")),     1),
        (invoke(STRING_LENGTH, string("ab")),    2),
        (invoke(STRING_LENGTH, string("abc")),   3),
        (invoke(STRING_LENGTH, string("tayne")), 5),

        (invoke(STRING_CONTAINS, string(""), string("")),                            True),
        (invoke(STRING_CONTAINS, string("a"), string("a")),                          True),
        (invoke(STRING_CONTAINS, string("abcde"), string("abc")),                    True),
        (invoke(STRING_CONTAINS, string("abcde"), string("bc")),                     True),
        (invoke(STRING_CONTAINS, string("car is red"), string("car")),               True),
        (invoke(STRING_CONTAINS, string("b"), string("a")),                          False),
        (invoke(STRING_CONTAINS, string("b"), string("abacus")),                     False),
        (invoke(STRING_CONTAINS, string("php-programmers"), string("self-respect")), False),

        (invoke(STRING_EMPTY, string("")),       True),
        (invoke(STRING_EMPTY, string(".")),      False),
        (invoke(STRING_EMPTY, string("hello!")), False),

        (invoke(STRING_REPEAT, string(""), integer(10)),       ""),
        (invoke(STRING_REPEAT, string("a"), integer(5)),       "aaaaa"),
        (invoke(STRING_REPEAT, string("hey"), integer(3)),     "heyheyhey"),
        (invoke(STRING_REPEAT, string("racecar"), integer(3)), "racecarracecarracecar"),

        (invoke(STRING_REVERSE, string("")),      ""),
        (invoke(STRING_REVERSE, string("abc")),   "cba"),
        (invoke(STRING_REVERSE, string("lol")),   "lol"),
        (invoke(STRING_REVERSE, string("jesus")), "susej"),

        (invoke(STRING_LOWERCASE, string("abc")),       "abc"),
        (invoke(STRING_LOWERCASE, string("AbC")),       "abc"),
        (invoke(STRING_LOWERCASE, string("LIMP 2017")), "limp 2017"),
        (invoke(STRING_LOWERCASE, string("Byxor")),     "byxor"),

        (invoke(STRING_UPPERCASE, string("abc")),       "ABC"),
        (invoke(STRING_UPPERCASE, string("AbC")),       "ABC"),
        (invoke(STRING_UPPERCASE, string("LIMP 2017")), "LIMP 2017"),
        (invoke(STRING_UPPERCASE, string("Byxor")),     "BYXOR"),

        (invoke(STRING_SPLIT, string(" "), string("a b c")),          ['a', 'b', 'c']),
        (invoke(STRING_SPLIT, string(", "), string("test, 1, 2, 3")), ['test', '1', '2', '3']),
        (invoke(STRING_SPLIT, string("-"), string("cars-the-movie")), ['cars', 'the', 'movie']),

        (invoke(STRING_JOIN, string(" "), list_of(string("1"), string("2"), string("3"))),
         "1 2 3"),
        
        (invoke(STRING_JOIN, string(" "), list_of(string("4"), string("5"), string("6"))),
         "4 5 6"),
        
        (invoke(STRING_JOIN, string("_::_"), list_of(string("tayne"), string("brain"))),
         "tayne_::_brain"),

    ])
