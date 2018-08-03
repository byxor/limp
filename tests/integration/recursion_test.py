import limp
import limp.environment as Environment
from tests.syntax import *
from limp.standard_library.math import *
from limp.standard_library.comparisons import *
from nose.tools import assert_equal


def test_basic_recursion():
    function_name = "factorial"
    parameter_name = "n"
    implementation = function([parameter_name],
                              if_statement(invoke(GREATER_THAN, parameter_name, integer(1)),
                                           invoke(MULTIPLY,
                                                  parameter_name,
                                                  invoke(function_name,
                                                         invoke(SUBTRACT, parameter_name, integer(1)))),
                                           integer(1)))

    environment = Environment.create_standard()
    environment.define(function_name, limp.evaluate(implementation, environment))

    data = [
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
    ]
    for parameter, expected_result in data:
        source_code = invoke(function_name, integer(parameter))
        result = limp.evaluate(source_code, environment)
        yield assert_equal, expected_result, result
