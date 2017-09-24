import limp
import limp.environment as Environment
from nose.tools import assert_equal


def test_tail_call_recursive_functions():
    environment = Environment.create_standard()

    recursive_function_definition = \
        """
        (define factorial (function (n)
          (if (> n 1)
            (* n (factorial (- n 1)))
            1)))
        """

    limp.evaluate(recursive_function_definition, environment)

    data = [
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
    ]
    for input_, expected_output in data:
        code = f"(factorial {input_})"
        output = limp.evaluate(code, environment)
        yield assert_equal, expected_output, output

