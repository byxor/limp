import limp
from nose.tools import assert_equal
from tests.syntax import *
from limp.standard_library.math import *
from limp.standard_library.comparisons import *


def test_stack_does_not_overflow():
    DEPTH = 100000

    ARGUMENT_NAME = 'n'

    CODE = invoke(
        tail_call_function(
            [ARGUMENT_NAME],
            if_statement(
                invoke(ARE_EQUAL, ARGUMENT_NAME, integer(0)),
                ARGUMENT_NAME,
                invoke(
                    ADD,
                    integer(1),
                    invoke(
                        self_reference(),
                        invoke(SUBTRACT, ARGUMENT_NAME, integer(1))
                    )
                ),
            )
        ),
        integer(DEPTH)
    )

    print(CODE)

    # assert_equal(DEPTH, limp.evaluate(CODE))
    
