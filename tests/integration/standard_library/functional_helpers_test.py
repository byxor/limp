import tests.helpers as Helpers
from tests.syntax import *
from tests.standard_library import *


TEMPORARY_NUMBERS = list_of(integer(1), integer(2), integer(3), integer(4))
TEMPORARY_NUMBER = symbol("n")


def test():
    Helpers.run_evaluation_test_on([
        (invoke(
            invoke(
                PARTIAL,
                ADD,
                integer(10)),
            integer(20)),
         30),
        
        (invoke(
            invoke(
                PARTIAL,
                MAP,
                IS_EVEN),
            TEMPORARY_NUMBERS),
         [False, True, False, True]),

        (invoke(
            invoke(
                PARTIAL,
                ADD,
                integer(10),
                integer(1),
                integer(2)),
            integer(20)),
         33),

        (invoke(
            invoke(
                PARTIAL,
                MAP,
                function(
                    [TEMPORARY_NUMBER],
                    invoke(
                        MULTIPLY,
                        TEMPORARY_NUMBER,
                        integer(2)))),
            TEMPORARY_NUMBERS),
         [2, 4, 6, 8]),

        (invoke(
            invoke(
                PARTIAL,
                FILTER,
                function(
                    [TEMPORARY_NUMBER],
                    invoke(
                        ARE_EQUAL,
                        TEMPORARY_NUMBER,
                        integer(1)))),
            TEMPORARY_NUMBERS),
         [1]),

        (invoke(
            CHAIN,
            integer(0),
            function(
                [TEMPORARY_NUMBER],
                invoke(
                    ADD,
                    TEMPORARY_NUMBER,
                    integer(10))),
            function(
                [TEMPORARY_NUMBER],
                invoke(
                    INTEGER_DIVIDE,
                    TEMPORARY_NUMBER,
                integer(2)))),
         5),

        (invoke(
            CHAIN,
            TEMPORARY_NUMBERS,
            invoke(
                PARTIAL,
                MAP,
                function(
                    [TEMPORARY_NUMBER],
                    invoke(
                        MULTIPLY,
                        TEMPORARY_NUMBER,
                        integer(2)))),
            invoke(
                PARTIAL,
                MAP,
                function(
                    [TEMPORARY_NUMBER],
                    invoke(
                        ADD,
                        TEMPORARY_NUMBER,
                        integer(1)))),
            invoke(
                PARTIAL,
                MAP,
                function(
                    [TEMPORARY_NUMBER],
                    invoke(
                        SUBTRACT,
                        TEMPORARY_NUMBER,
                        integer(1)))),
            invoke(
                PARTIAL,
                FILTER,
                function(
                    [TEMPORARY_NUMBER],
                    invoke(
                        ARE_EQUAL,
                        invoke(
                            MODULO,
                            TEMPORARY_NUMBER,
                            integer(4)),
                        integer(0)))),
            invoke(
                PARTIAL,
                REDUCE,
                ADD)),
         12)

    ])
