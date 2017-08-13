import limp
from unittest import TestCase


class InterfaceTest(TestCase):

    def test_that_code_can_be_evaluated_with_a_simple_import(self):
        evaluate = limp.evaluate
        self.assertEqual(10, evaluate('10'))
        self.assertEqual(2, evaluate('(- 5 3)'))
        self.assertEqual(100, evaluate('(* 50 2)'))
    
