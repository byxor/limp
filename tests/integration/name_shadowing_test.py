import limp
import limp.environment as Environment
from nose.tools import assert_equal


def test_function_parameters_can_shadow_globally_defined_variables():
    variable_name = 'n'
    original_value = 0
    function_name = "number"
    function_definition = f"(define {function_name} (function ({variable_name}) {variable_name}))"
    
    environment = Environment.create_empty()
    environment.define(variable_name, original_value)

    run = lambda code: limp.evaluate(code, environment)
    variable_is_unchanged = lambda: (assert_equal, original_value, run(variable_name))
    run(function_definition)

    run(f"({function_name} 1)")

    yield variable_is_unchanged()
