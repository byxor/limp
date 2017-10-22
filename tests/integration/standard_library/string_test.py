import tests.helpers as Helpers
from tests.syntax import *
from limp.standard_library.strings import *


def test():
    Helpers.run_evaluation_test_on([

        (invoke(CONCATENATE, string("foo"), string("bar")),
         "foobar"),
        
        (invoke(CONCATENATE, string("hello"), string(" "), string("there")),
         "hello there"),

        (invoke(STRIP, string(" x ")),                "x"),
        (invoke(STRIP, string(" abc ")),              "abc"),
        (invoke(STRIP, string(" x \t\n")),            "x"),
        (invoke(STRIP, string("hello \n\t\n there")), "hello \n\t\n there"),

        (invoke(LENGTH, string("")),      0),
        (invoke(LENGTH, string("a")),     1),
        (invoke(LENGTH, string("ab")),    2),
        (invoke(LENGTH, string("abc")),   3),
        (invoke(LENGTH, string("tayne")), 5),

        (invoke(CONTAINS, string(""), string("")),                            True),
        (invoke(CONTAINS, string("a"), string("a")),                          True),
        (invoke(CONTAINS, string("abcde"), string("abc")),                    True),
        (invoke(CONTAINS, string("abcde"), string("bc")),                     True),
        (invoke(CONTAINS, string("car is red"), string("car")),               True),
        (invoke(CONTAINS, string("b"), string("a")),                          False),
        (invoke(CONTAINS, string("b"), string("abacus")),                     False),
        (invoke(CONTAINS, string("php-programmers"), string("self-respect")), False),

        (invoke(EMPTY, string("")),       True),
        (invoke(EMPTY, string(".")),      False),
        (invoke(EMPTY, string("hello!")), False),

        (invoke(REPEAT, string(""), integer(10)),       ""),
        (invoke(REPEAT, string("a"), integer(5)),       "aaaaa"),
        (invoke(REPEAT, string("hey"), integer(3)),     "heyheyhey"),
        (invoke(REPEAT, string("racecar"), integer(3)), "racecarracecarracecar"),

        (invoke(REVERSE, string("")),      ""),
        (invoke(REVERSE, string("abc")),   "cba"),
        (invoke(REVERSE, string("lol")),   "lol"),
        (invoke(REVERSE, string("jesus")), "susej"),

        (invoke(LOWERCASE, string("abc")),       "abc"),
        (invoke(LOWERCASE, string("AbC")),       "abc"),
        (invoke(LOWERCASE, string("LIMP 2017")), "limp 2017"),
        (invoke(LOWERCASE, string("Byxor")),     "byxor"),

        (invoke(UPPERCASE, string("abc")),       "ABC"),
        (invoke(UPPERCASE, string("AbC")),       "ABC"),
        (invoke(UPPERCASE, string("LIMP 2017")), "LIMP 2017"),
        (invoke(UPPERCASE, string("Byxor")),     "BYXOR"),

        (invoke(SPLIT, string(" "), string("a b c")),          ['a', 'b', 'c']),
        (invoke(SPLIT, string(", "), string("test, 1, 2, 3")), ['test', '1', '2', '3']),
        (invoke(SPLIT, string("-"), string("cars-the-movie")), ['cars', 'the', 'movie']),

        (invoke(JOIN, string(" "), list_of(string("1"), string("2"), string("3"))),
         "1 2 3"),
        
        (invoke(JOIN, string(" "), list_of(string("4"), string("5"), string("6"))),
         "4 5 6"),
        
        (invoke(JOIN, string("_::_"), list_of(string("tayne"), string("brain"))),
         "tayne_::_brain"),

    ])
