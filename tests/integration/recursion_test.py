import limp
import limp.environment as Environment
from tests.syntax import *
from limp.standard_library import *
from limp.standard_library.math import *
from limp.standard_library.comparisons import *
from unittest import TestCase


class TailCallRecursion(TestCase):

    FUNCTION_NAME = "factorial"
    ARGUMENT_NAME = "n"

    IMPLEMENTATION = function(
        [ARGUMENT_NAME],
        if_statement(
            invoke(GREATER_THAN, ARGUMENT_NAME, integer(1)),
            invoke(
                MULTIPLY,
                ARGUMENT_NAME,
                invoke(
                    FUNCTION_NAME,
                    invoke(SUBTRACT, ARGUMENT_NAME, integer(1))
                )
            ),
            integer(1)
        )
    )

    def setUp(self):
        self.environment = Environment.create_standard()
        self.evaluate = lambda code: limp.evaluate(code, self.environment)
        self.evaluate(
            define(
                TailCallRecursion.FUNCTION_NAME,
                TailCallRecursion.IMPLEMENTATION
            )
        )

    def test(self):
        data = [
            (1, 1),
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120),
            (6, 720),
        ]
        for parameter, expected_output in data:
            output = self.evaluate(invoke(TailCallRecursion.FUNCTION_NAME, str(parameter)))
            self.assertEqual(expected_output, output)
