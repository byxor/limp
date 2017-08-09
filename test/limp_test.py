import limp.types as types
from unittest import TestCase
from limp.limp import *


class MiscellaneousLimpTest(TestCase):

    def test_tokenising_source_code(self):
        data = [
            ('()', ['(', ')']),
            ('(abc)', ['(', 'abc', ')']),
            ('(abc 1 2 3)', ['(', 'abc', '1', '2', '3', ')'])
        ]
        for source_code, expected_tokens in data:
            self.assertEqual(expected_tokens, tokenize(source_code))

    def test_atomising_symbols(self):
        data = [
            ('abc', 'abc', types.Symbol),
            ('def', 'def', types.Symbol),
            ('123', 123, int),
            ('456', 456, int),
            ('1.2', 1.2, float),
            ('2.4', 2.4, float)
        ]
        for symbol, expected_atom_value, expected_atom_type in data:
            atom = atomize(symbol)
            self.assertEqual(atom, expected_atom_value)
            self.assertEqual(type(atom), expected_atom_type)

    def test_parsing_source_code(self):
        data = [
            ('(+ 1 2)', [types.Symbol('+'), 1, 2]),
            ('(reverse (1 2 3 4 5))', ['reverse', [1, 2, 3, 4, 5]])
        ]
        for source_code, expected_abstract_syntax_tree in data:
            self.assertEqual(expected_abstract_syntax_tree, parse(source_code))
            

class SyntaxTreeBuilderTest(TestCase):

    def setUp(self):
        self.build_from = build_syntax_tree
    
    def test_empty_tokens_raise_SyntaxError(self):
        self.assertRaises(SyntaxError, self.build_from, [])

    def test_unmatched_closing_bracket_raises_SyntaxError(self):
        self.assertRaises(SyntaxError, self.build_from, [')'])
    
    def test_valid_tokens(self):
        data = [
            (['(', ')'], []),
            (['(', 'abc', ')'], ['abc']),
            (['(', '+', '1', '2', ')'], [types.Symbol('+'), 1, 2]),
            (['(', '/', '10', '(', '-', '5', '3', ')', ')'], [types.Symbol('/'), 10, [types.Symbol('-'), 5, 3]])
        ]
        for tokens, expected_tree in data:
            self.assertEqual(
                expected_tree,
                self.build_from(tokens)
            )
            

class EvaluationTest(TestCase):

    def setUp(self):
        environment = standard_environment()
        self.run = lambda source_code: evaluate(parse(source_code), environment)

    def test_constants(self):
        data = [
            ('10', 10),
            ('3.5', 3.5)
        ]
        for literal, expected_result in data:
            self.assertEqual(expected_result, self.run(literal))

    def test_accessing_non_existent_variable_raises_NameError(self):
        self.assertRaises(NameError, self.run, 'x')
        self.assertRaises(NameError, self.run, 'y')
        self.assertRaises(NameError, self.run, 'z')
    
    def test_defining_and_accessing_variables(self):
        self.run('(define x 10)')
        self.run('(define y 20)')
        self.run('(define z 30)')
        self.assertEqual(10, self.run('x'))
        self.assertEqual(10, self.run('x'))
        self.assertEqual(20, self.run('y'))
        self.assertEqual(20, self.run('y'))
        self.assertEqual(30, self.run('z'))
        self.assertEqual(30, self.run('z'))

    def test_standard_library_procedures(self):
        data = [
            ('(+ 1 1)', 2),
            ('(+ 2 3)', 5),
            ('(- 1 1)', 0),
            ('(- 4 2)', 2),
            ('(* 2 3)', 6),
            ('(* 4 1)', 4),
            ('(/ 4 2)', 2),
            ('(/ 1 2)', 0.5),
            ('(// 1 2)', 0),
            ('(// 5 2)', 2)
        ]
        for source_code, expected_result in data:
            self.assertEqual(expected_result, self.run(source_code))
        
