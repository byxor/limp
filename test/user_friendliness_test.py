import limp
import limp.environment
from unittest import TestCase


class Tests(TestCase):

    def setUp(self):
        self.run = limp.evaluate
    
    def test_that_code_can_be_evaluated_with_a_simple_import(self):
        self.assertEqual(10, self.run('10'))
        self.assertEqual(2, self.run('(- 5 3)'))
        self.assertEqual(100, self.run('(* 50 2)'))

    def test_that_clean_environment_is_created_automatically(self):
        self.run('(define x 10)')
        self.assertRaises(Exception, self.run, 'x')
        
    def test_that_environment_can_be_provided(self):
        environment = limp.environment.create_standard()
        run = lambda source_code: self.run(source_code, environment)
        run('(define x 10)')
        run('(define y 20)')
        run('(define z 30)')
        self.assertEqual(10, run('x'))
        self.assertEqual(20, run('y'))
        self.assertEqual(30, run('z'))
    
