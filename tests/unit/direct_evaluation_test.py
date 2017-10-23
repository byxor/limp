import limp.environment as Environment
import limp.errors as Errors
import limp.types as Types
import tests.helpers as Helpers
from tests.syntax import *
from limp.standard_library import *
from limp.standard_library.math import *
from copy import copy
from nose.tools import *


### Numeric Types ###

def test_decimal_integers():
    data = [
        (integer(0),           0),
        (integer(10),          10),
        (integer(23),          23),
        (negative(integer(4)), -4),
        (positive(integer(4)), +4),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Integer)


def test_hexadecimal_integers():
    data = [
        (hexadecimal(0x0),               0x0),
        (hexadecimal(0x123),             0x123),
        (hexadecimal(0xDEADA55),         0xDEADA55),
        (negative(hexadecimal(0x1)),     -0x1),
        (negative(hexadecimal(0xBEEF)),  -0xBEEF),
        (positive(hexadecimal(0xB00B5)), +0xB00B5),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Hexadecimal)


def test_binary_integers():
    data = [
        (binary(0b0),             0b0),
        (binary(0b1),             0b1),
        (binary(0b101),           0b101),
        (negative(binary(0b1)),   -0b1),
        (negative(binary(0b111)), -0b111),
        (positive(binary(0b10)),  +0b10),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Binary)


def test_floats():
    data = [
        (float_(0),               0.0),
        (float_(0.5),             0.5),
        (float_(2.3),             2.3),
        (float_(1.23456789),      1.23456789),
        (negative(float_(2.5)),   -2.5),
        (negative(float_(60.12)), -60.12),
        (positive(float_(20.3)),  +20.3),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Float)


def test_booleans():
    data = [
        (boolean(True),  True),
        (boolean(False), False),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Boolean)

        
def test_strings():
    data = [
        (string("Hey"),          "Hey"),
        (string("Hello there!"), "Hello there!"),
        (string("\n\n\n"),       "\n\n\n"),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.String)

        
### Symbols ###        
        
def test_accessing_variables():
    data = [
        (symbol('x'),   10),
        (symbol('y'),   20),
        (symbol('z'),   30),
        (symbol('foo'), 100),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Symbol)

        
def test_exception_raised_when_accessing_non_existent_variable():
    data = [
        symbol('year'),
        symbol('boy'),
        symbol('bones'),
        symbol('dyliams'),
        symbol('antichav'),
        symbol('sesh')
    ]
    for contents in data:
        symbol_ = Types.Symbol(contents, Environment.create_empty())
        yield assert_raises, Errors.UndefinedSymbol, symbol_.evaluate


### Invocations ###

def test_invoking_functions():
    data = [
        ([symbol('add'), integer(1), integer(2)],                   3),
        ([symbol('subtract'), integer(10), integer(5)],             5),
        ([symbol('multiply'), integer(2), integer(3), integer(5)], 30),
        ([symbol('return10')],                                     10),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Invocation)


def test_invoking_anonymous_functions():
    data = [
        ([[Types.Function.KEYWORD, [], integer(0)]],                                0),
        ([[Types.Function.KEYWORD, [], integer(4)]],                                4),
        ([[Types.Function.KEYWORD, [symbol('n')], symbol('n')], integer(0)],                        0),
        ([[Types.Function.KEYWORD, [symbol('n')], symbol('n')], integer(9)],                        9),
        
        ([[Types.Function.KEYWORD, [symbol('a'), symbol('b')], [ADD, symbol('a'), symbol('b')]],
          integer(10), integer(5)], 15),

        ([[Types.Function.KEYWORD, [symbol('a'), symbol('b')], [ADD, symbol('a'), symbol('b')]],
          integer(20), integer(0)], 20),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Invocation)


def test_invoking_functions_with_variables():
    data = [
        ([symbol('add'), symbol('x'), symbol('y')],      30),
        ([symbol('subtract'), symbol('z'), symbol('x')], 20),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Invocation)

        
def test_exception_raised_when_invoking_non_existent_function():
    data = [
        ([symbol('reset')]),
    ]
    for contents in data:
        invocation = Types.Invocation(contents, Environment.create_empty())
        yield assert_raises, Errors.UndefinedSymbol, invocation.evaluate
        

### Definitions ###

def test_defining_variables():
    data = [
        ([Types.Definition.KEYWORD, symbol('age'), integer(20)], symbol('age'), 20),
        ([Types.Definition.KEYWORD, symbol('abc'), integer(52)], symbol('abc'), 52),
    ]
    for definition_contents, symbol_contents, expected_value in data:
        environment = Environment.create_empty()
        definition = Types.Definition(definition_contents, environment)
        symbol_ = Types.Symbol(symbol_contents, environment)
        definition.evaluate()
        value = symbol_.evaluate()
        yield assert_equals, expected_value, value


def test_redefining_variables_raises_an_exception():
    data = [symbol('foo'), symbol('bar'), symbol('baz')]
    for name in data:
        value = string("does not matter")
        definition = Types.Definition([Types.Definition.KEYWORD, name, value], Environment.create_empty())
        definition.evaluate()
        yield assert_raises, Errors.RedefinedSymbol, definition.evaluate


### Sequential Evaluators ###

def test_sequential_evaluators():
    environment = Helpers.sample_environment()

    sequential_evaluator = Types.SequentialEvaluator([
        Types.SequentialEvaluator.KEYWORD,
        [Types.Definition.KEYWORD, symbol('one'),   integer(1)],
        [Types.Definition.KEYWORD, symbol('two'),   integer(2)],
        [Types.Definition.KEYWORD, symbol('three'), integer(3)],
    ], environment)

    sequential_evaluator.evaluate()
    
    data = [
        (symbol('one'),   1),
        (symbol('two'),   2),
        (symbol('three'), 3),
    ]
    for symbol_, expected_value in data:
        value = environment.resolve(symbol_)
        yield assert_equals, expected_value, value


def test_sequential_evaluators_raise_an_error_when_not_needed():
    data = [
        [Types.SequentialEvaluator.KEYWORD, integer(0)],
        [Types.SequentialEvaluator.KEYWORD, [symbol('+'), integer(1), integer(2)]],
        [Types.SequentialEvaluator.KEYWORD, string("foo")],
    ]
    for contents in data:
        sequential_evaluator = Types.SequentialEvaluator(contents, Helpers.sample_environment())
        yield (assert_raises,
               Errors.UnnecessarySequentialEvaluator,
               sequential_evaluator.evaluate)


def test_sequential_evaluators_return_value_of_last_form():
    data = [
        ([Types.SequentialEvaluator.KEYWORD, integer(1), integer(2), integer(3)],  3),
        ([Types.SequentialEvaluator.KEYWORD, integer(5), integer(6), integer(7)],  7),
        ([Types.SequentialEvaluator.KEYWORD, integer(3), string("tayne")],         "tayne"),
    ]
    for contents, expected_value in data:
        sequential_evaluator = Types.SequentialEvaluator(contents, Helpers.sample_environment())
        value = sequential_evaluator.evaluate()
        yield assert_equals, expected_value, value
        

### Conditionals ###

def test_simple_conditional_statements():
    data = [
        ([Types.SimpleConditional.KEYWORD, boolean(True),  string("yes!"), string("no!")], "yes!"),
        ([Types.SimpleConditional.KEYWORD, boolean(False), string("yes!"), string("no!")], "no!"),
        ([Types.SimpleConditional.KEYWORD, boolean(True),  integer(5)],                    5),
        ([Types.SimpleConditional.KEYWORD, boolean(False), integer(4)],                    None),

        ([Types.SimpleConditional.KEYWORD,
          [symbol('>'), integer(10), integer(0)], boolean(True)],
         True),

        ([Types.SimpleConditional.KEYWORD,
          [symbol('='), integer(1), integer(1)],  [symbol('+'), integer(10), integer(10)]],
         20),
        
        ([Types.SimpleConditional.KEYWORD,
          [symbol('='), integer(1), integer(0)], integer(0), [symbol('-'), integer(10), integer(5)]],
         5),
    ]
    for contents, expected_value in data:
        conditional = Types.SimpleConditional(contents, Helpers.sample_environment())
        value = conditional.evaluate()
        yield assert_equals, expected_value, value


def test_complex_conditional_statements():
    data = [
        ([Types.ComplexConditional.KEYWORD, [boolean(True), integer(0)]],  0),
        ([Types.ComplexConditional.KEYWORD, [boolean(True), integer(1)]],  1),
        ([Types.ComplexConditional.KEYWORD, [boolean(False), integer(2)]], None),
        
        ([Types.ComplexConditional.KEYWORD, [boolean(False), integer(0)], [boolean(True), integer(1)]], 1),

        ([Types.ComplexConditional.KEYWORD,
          [[symbol('='), integer(0), integer(1)], string("NotThisOne")],
          [[symbol('='), integer(0), integer(2)], string("NorThisOne")],
          [[symbol('='), integer(0), integer(0)], [symbol('concatenate'), string("This"), string("One")]],
          [[symbol('='), integer(0), integer(3)], string("NorNorThisOne")]], "ThisOne")
    ]
    for contents, expected_value in data:
        conditional = Types.ComplexConditional(contents, Helpers.sample_environment())
        value = conditional.evaluate()
        yield assert_equals, expected_value, value
    

### Functions ###

def test_functions_with_no_arguments():
    data = [
        ([Types.Function.KEYWORD, integer(1)],                 1),
        ([Types.Function.KEYWORD, string("foo")],              "foo"),
        ([Types.Function.KEYWORD, [], integer(10)],            10),
        ([Types.Function.KEYWORD, [], integer(20)],            20),
        ([Types.Function.KEYWORD, [], float_(0.1)],           0.1),
        
        ([Types.Function.KEYWORD, [], [symbol('+'), integer(1), integer(2)]], 3),
    ]
    for contents, expected_value in data:
        function = Types.Function(contents, Environment.create_standard())
        internal_function = function.evaluate()
        yield assert_equals, expected_value, internal_function()
   

def test_functions_with_arguments():
    data = [
        ([Types.Function.KEYWORD, [symbol('x')], symbol('x')], [10], 10),
        ([Types.Function.KEYWORD, [symbol('x')], symbol('x')], [9],  9),
        ([Types.Function.KEYWORD, [symbol('y')], symbol('y')], [2],  2),
        ([Types.Function.KEYWORD, [symbol('y')], symbol('y')], [1],  1),

        ([Types.Function.KEYWORD, [symbol('n')], [EXPONENT, symbol('n'), integer(2)]], [1], 1),
        ([Types.Function.KEYWORD, [symbol('n')], [EXPONENT, symbol('n'), integer(2)]], [2], 4),
        ([Types.Function.KEYWORD, [symbol('n')], [EXPONENT, symbol('n'), integer(2)]], [3], 9),
        ([Types.Function.KEYWORD, [symbol('n')], [EXPONENT, symbol('n'), integer(2)]], [4], 16),
        ([Types.Function.KEYWORD, [symbol('n')], [EXPONENT, symbol('n'), integer(2)]], [5], 25),

        ([Types.Function.KEYWORD, [symbol('a'), symbol('b')], [ADD, symbol('a'), symbol('b')]], [0, 0], 0),
        ([Types.Function.KEYWORD, [symbol('a'), symbol('b')], [ADD, symbol('a'), symbol('b')]], [0, 1], 1),
        ([Types.Function.KEYWORD, [symbol('a'), symbol('b')], [ADD, symbol('a'), symbol('b')]], [5, 3], 8),
    ]
    for contents, arguments, expected_value in data:
        function = Types.Function(contents, Environment.create_standard())
        internal_function = function.evaluate()
        yield assert_equals, expected_value, internal_function(*arguments)
    

### Lists ###

def test_lists():
    data = [
        ([Types.List.KEYWORD, integer(1), integer(2), integer(3)], [1, 2, 3]),
        ([Types.List.KEYWORD, string("celery"), string("man")],    ["celery", "man"]),
    ]
    for contents, expected_value in data:
        list_ = Types.List(contents, Environment.create_standard())
        yield assert_equals, expected_value, list_.evaluate()
