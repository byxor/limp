import limp.atom as Atom
import limp.environment as Environment
import limp.syntax_tree as SyntaxTree
import limp.tokens as Tokens
import limp.types as Types
import limp.evaluation as Evaluation
from unittest import TestCase


class BuildingTests(TestCase):

    def setUp(self):
        self.build_from = SyntaxTree.create_from

    def test_empty_tokens_raise_SyntaxError(self):
        self.assertRaises(SyntaxError, self.build_from, [])

    def test_unmatched_closing_bracket_raises_SyntaxError(self):
        self.assertRaises(SyntaxError, self.build_from, [')'])

    def test_valid_tokens(self):
        data = [
            (['(', ')'], []),
            (['(', 'abc', ')'], ['abc']),
            (['(', '+', '1', '2', ')'], [Types.Symbol('+'), 1, 2]),
            (['(', '/', '10', '(', '-', '5', '3', ')', ')'],
             [Types.Symbol('/'), 10, [Types.Symbol('-'), 5, 3]])
        ]
        for tokens, expected_tree in data:
            self.assertEqual(
                expected_tree,
                self.build_from(tokens)
            )
