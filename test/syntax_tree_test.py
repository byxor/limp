import limp.atom as atom
import limp.environments as environments
import limp.syntax_tree as syntax_tree
import limp.tokens as tokens
import limp.types as types
import limp.evaluation as evaluation
from unittest import TestCase


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
            (['(', '/', '10', '(', '-', '5', '3', ')', ')'],
             [types.Symbol('/'), 10, [types.Symbol('-'), 5, 3]])
        ]
        for tokens, expected_tree in data:
            self.assertEqual(
                expected_tree,
                self.build_from(tokens)
            )
