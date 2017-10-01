import limp.environment as Environment
import limp.errors as Errors
import limp.types as Types
import test.helpers as Helpers
from copy import copy
from nose.tools import *


### Numeric Types ###

def test_decimal_integers():
    data = [
        ('0',  0),
        ('10', 10),
        ('23', 23),
        ('-4', -4),
        ('+4', +4),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Integer)


def test_hexadecimal_integers():
    data = [
        ('0x0',       0x0),
        ('0x123',     0x123),
        ('0xDEADA55', 0xDEADA55),
        ('-0x1',      -0x1),
        ('-0xBEEF',   -0xBEEF),
        ('+0xB00B5',  +0xB00B5),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Hexadecimal)


def test_binary_integers():
    data = [
        ('0b0',    0b0),
        ('0b1',    0b1),
        ('0b101',  0b101),
        ('-0b1',   -0b1),
        ('-0b111', -0b111),
        ('+0b10',  +0b10),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Binary)


def test_floats():
    data = [
        ('0',          0.0),
        ('0.5',        0.5),
        ('2.3',        2.3),
        ('1.23456789', 1.23456789),
        ('-2.5',       -2.5),
        ('-60.12',     -60.12),
        ('+20.3',      +20.3),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Float)


def test_booleans():
    data = [
        ('true',  True),
        ('false', False),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Boolean)

        
def test_strings():
    data = [
        ('"Hey"',          "Hey"),
        ('"Hello there!"', "Hello there!"),
        ('"\n\n\n"',      "\n\n\n"),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.String)

        
### Symbols ###        
        
def test_accessing_variables():
    data = [
        ('x',   10),
        ('y',   20),
        ('z',   30),
        ('foo', 100),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Symbol)

        
def test_exception_raised_when_accessing_non_existent_variable():
    data = ['year', 'boy', 'bones', 'dyliams', 'antichav', 'sesh']
    for contents in data:
        symbol = Types.Symbol(contents, Environment.create_empty())
        yield assert_raises, Errors.UndefinedSymbol, symbol.evaluate


### Invocations ###
        
def test_invoking_functions():
    data = [
        (['add', '1', '2'],           3),
        (['subtract', '10', '5'],     5),
        (['multiply', '2', '3', '5'], 30),
        (['return10'],                10),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Invocation)


def test_invoking_anonymous_functions():
    data = [
        ([['function', [], '0']],                                0),
        ([['function', [], '4']],                                4),
        ([['function', ['n'], 'n'], '0'],                        0),
        ([['function', ['n'], 'n'], '9'],                        9),
        ([['function', ['a', 'b'], ['+', 'a', 'b']], '10', '5'], 15),
        ([['function', ['a', 'b'], ['+', 'a', 'b']], '20', '0'], 20),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Invocation)


def test_invoking_functions_with_variables():
    data = [
        (['add', 'x', 'y'],      30),
        (['subtract', 'z', 'x'], 20),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Invocation)

        
def test_exception_raised_when_invoking_non_existent_function():
    data = [
        (['reset']),
    ]
    for contents in data:
        invocation = Types.Invocation(contents, Environment.create_empty())
        yield assert_raises, Errors.UndefinedSymbol, invocation.evaluate
        

### Definitions ###

def test_defining_variables():
    data = [
        (['define', 'age', '20'], 'age', 20),
        (['define', 'abc', '52'], 'abc', 52),
    ]
    for definition_contents, symbol_contents, expected_value in data:
        environment = Environment.create_empty()
        definition = Types.Definition(definition_contents, environment)
        symbol = Types.Symbol(symbol_contents, environment)
        definition.evaluate()
        value = symbol.evaluate()
        yield assert_equals, expected_value, value


def test_redefining_variables_raises_an_exception():
    data = ['foo', 'bar', 'baz']
    for name in data:
        value = '"does not matter"'
        definition = Types.Definition(['define', name, value], Environment.create_empty())
        definition.evaluate()
        yield assert_raises, Errors.RedefinedSymbol, definition.evaluate


### Sequential Evaluators ###

def test_sequential_evaluators():
    environment = Helpers.sample_environment()

    sequential_evaluator = Types.SequentialEvaluator([
        'do',
        ['define', 'one',   '1'],
        ['define', 'two',   '2'],
        ['define', 'three', '3'],
    ], environment)

    sequential_evaluator.evaluate()
    
    data = [
        ('one',   1),
        ('two',   2),
        ('three', 3),
    ]
    for symbol, expected_value in data:
        value = environment.resolve(symbol)
        yield assert_equals, expected_value, value


def test_sequential_evaluators_raise_an_error_when_not_needed():
    data = [
        ['do', '0'],
        ['do', ['+', '1', '2']],
        ['do', '"foo"'],
    ]
    for contents in data:
        sequential_evaluator = Types.SequentialEvaluator(contents, Helpers.sample_environment())
        yield (assert_raises,
               Errors.UnnecessarySequentialEvaluator,
               sequential_evaluator.evaluate)


def test_sequential_evaluators_return_value_of_last_form():
    data = [
        (['do', '1', '2', '3'],  3),
        (['do', '5', '6', '7'],  7),
        (['do', '3', '"tayne"'], "tayne"),
    ]
    for contents, expected_value in data:
        sequential_evaluator = Types.SequentialEvaluator(contents, Helpers.sample_environment())
        value = sequential_evaluator.evaluate()
        yield assert_equals, expected_value, value
        

### Conditionals ###

def test_simple_conditional_statements():
    data = [
        (['if', 'true',  '"yes!"', '"no!"'], "yes!"),
        (['if', 'false', '"yes!"', '"no!"'], "no!"),
        (['if', 'true',  '5'],               5),
        (['if', 'false', '4'],               None),

        (['if', ['>', '10', '0'], 'true'],                True),
        (['if', ['=', '1', '1'],  ['+', '10', '10']],     20),
        (['if', ['=', '1', '0'],  '0', ['-', '10', '5']], 5),
    ]
    for contents, expected_value in data:
        conditional = Types.SimpleConditional(contents, Helpers.sample_environment())
        value = conditional.evaluate()
        yield assert_equals, expected_value, value


def test_complex_conditional_statements():
    data = [
        (['condition', ['true', '0']], 0),
        (['condition', ['true', '1']], 1),
        (['condition', ['false', '2']], None),
        
        (['condition', ['false', '0'], ['true', '1']], 1),

        (['condition',
          [['=', '0', '1'], '"NotThisOne"'],
          [['=', '0', '2'], '"NorThisOne"'],
          [['=', '0', '0'], ['concatenate', '"This"', '"One"']],
          [['=', '0', '3'], '"NorNorThisOne"']], "ThisOne")
    ]
    for contents, expected_value in data:
        conditional = Types.ComplexConditional(contents, Helpers.sample_environment())
        value = conditional.evaluate()
        yield assert_equals, expected_value, value
    

### Functions ###

def test_functions_with_no_arguments():
    data = [
        (['function', [], '10'],            10),
        (['function', [], '20'],            20),
        (['function', [], '0.1'],           0.1),
        (['function', [], ['+', '1', '2']], 3),
    ]
    for contents, expected_value in data:
        function = Types.Function(contents, Environment.create_standard())
        internal_function = function.evaluate()
        yield assert_equals, expected_value, internal_function()
   

def test_functions_with_arguments():
    data = [
        (['function', ['x'], 'x'], [10], 10),
        (['function', ['x'], 'x'], [9],  9),
        (['function', ['y'], 'y'], [2],  2),
        (['function', ['y'], 'y'], [1],  1),

        (['function', ['n'], ['**', 'n', '2']], [1], 1),
        (['function', ['n'], ['**', 'n', '2']], [2], 4),
        (['function', ['n'], ['**', 'n', '2']], [3], 9),
        (['function', ['n'], ['**', 'n', '2']], [4], 16),
        (['function', ['n'], ['**', 'n', '2']], [5], 25),

        (['function', ['a', 'b'], ['+', 'a', 'b']], [0, 0], 0),
        (['function', ['a', 'b'], ['+', 'a', 'b']], [0, 1], 1),
        (['function', ['a', 'b'], ['+', 'a', 'b']], [5, 3], 8),
    ]
    for contents, arguments, expected_value in data:
        function = Types.Function(contents, Environment.create_standard())
        internal_function = function.evaluate()
        yield assert_equals, expected_value, internal_function(*arguments)
    

### Lists ###

def test_lists():
    data = [
        (['list', '1', '2', '3'],       [1, 2, 3]),
        (['list', '"celery"', '"man"'], ["celery", "man"]),
    ]
    for contents, expected_value in data:
        list_ = Types.List(contents, Environment.create_standard())
        yield assert_equals, expected_value, list_.evaluate()
