import limp.environments as environments
import limp.evaluation as evaluation
import limp.syntax_tree as syntax_tree
import limp.tokens as tokens
from unittest import TestCase


class Tests(TestCase):

    def setUp(self):
        make_evaluatable = lambda source_code: syntax_tree.create_from(tokens.create_from(source_code))
        environment = environments.create_standard()
        self.run = lambda source_code: evaluation.execute(make_evaluatable(source_code), environment)

    def test_literals(self):
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
        self.assertEqual(20, self.run('y'))
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
