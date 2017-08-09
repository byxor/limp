import limp.atom as atom
import limp.environments as environments
import limp.syntax_tree as syntax_tree
import limp.tokens as tokens
import limp.types as types
import limp.evaluation as evaluation
from unittest import TestCase


class MiscellaneousLimpTest(TestCase):

    def test_tokenising_source_code(self):
        data = [
            ('()', ['(', ')']),
            ('(abc)', ['(', 'abc', ')']),
            ('(abc 1 2 3)', ['(', 'abc', '1', '2', '3', ')'])
        ]
        for source_code, expected_tokens in data:
            self.assertEqual(expected_tokens, tokens.create_from(source_code))

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
            atom_ = atom.create_from(symbol)
            self.assertEqual(atom_, expected_atom_value)
            self.assertEqual(type(atom_), expected_atom_type)


class SyntaxTreeBuilderTest(TestCase):

    def setUp(self):
        self.build_from = syntax_tree.create_from

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
        environment = environments.create_standard()
        self.run = lambda source_code: evaluation.execute(syntax_tree.create_from(tokens.create_from(source_code)), environment)

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
        
