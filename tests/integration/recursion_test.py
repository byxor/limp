import limp
import limp.environment as Environment
from tests.syntax import *
from unittest import TestCase


class TailCallRecursion(TestCase):

    FUNCTION_NAME = "factorial"
    ARGUMENT_NAME = "n"
    IMPLEMENTATION = function(
        [ARGUMENT_NAME],
        if_statement(
            invoke(">", ARGUMENT_NAME, "1"),
            invoke(
                "*",
                ARGUMENT_NAME,
                invoke(
                    FUNCTION_NAME,
                    invoke("-", ARGUMENT_NAME, "1")
                )
            ),
            "1"
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

