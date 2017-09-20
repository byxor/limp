import limp.types as Types
import test.helpers as Helpers
from copy import copy
from nose.tools import assert_equals


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


### Booleans ###

def test_booleans():
    data = [
        ('true',  True),
        ('false', False),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Boolean)


### Strings ###

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


def test_invoking_functions_with_variables():
    data = [
        (['add', 'x', 'y'],      30),
        (['subtract', 'z', 'x'], 20),
    ]
    for contents, expected_value in data:
        yield Helpers.assert_form_evaluates_to(expected_value, contents, Types.Invocation)


### Definitions ###

def test_defining_variables():

    data = [
        (['define', 'age', '20'], 'age', 20),
        (['define', 'abc', '52'], 'abc', 52),
    ]
    for definition_contents, symbol_contents, expected_value in data:
        environment = copy(Helpers.SIMPLE_ENVIRONMENT)
        definition = Types.Definition(definition_contents, environment)
        symbol = Types.Symbol(symbol_contents, environment)
        definition.evaluate()
        value = symbol.evaluate()
        yield assert_equals, expected_value, value


### Sequential Evaluators ###

def test_sequential_evaluators():
    environment = Helpers.SIMPLE_ENVIRONMENT

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
        value = environment[symbol]
        yield assert_equals, expected_value, value


### Conditionals ###

def test_simple_conditional_statements():
    data = [
        (['if', 'true',  '"yes!"', '"no!"'], "yes!"),
        (['if', 'false', '"yes!"', '"no!"'], "no!"),
        (['if', 'true',  '5'],               5),
        (['if', 'false', '4'],               None),
    ]
    for contents, expected_value in data:
        conditional = Types.Conditional(contents, Helpers.SIMPLE_ENVIRONMENT)
        value = conditional.evaluate()
        yield assert_equals, expected_value, value

        
def test_complex_conditional_statements():
    data = [
        (['if', ['>', '10', '0'], 'true'],                True),
        (['if', ['=', '1', '1'],  ['+', '10', '10']],     20),
        (['if', ['=', '1', '0'],  '0', ['-', '10', '5']], 5),
    ]
    for contents, expected_value in data:
        conditional = Types.Conditional(contents, Helpers.SIMPLE_ENVIRONMENT)
        value = conditional.evaluate()
        yield assert_equals, expected_value, value
    
