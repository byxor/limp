import limp
import test.helpers as Helpers
from nose.tools import assert_equals


def test_mathematical_functions():
    data = [
        ('(+ 1 1)',    2),
        ('(+ 2 3)',    5),
        ('(- 1 1)',    0),
        ('(- 4 2)',    2),
        ('(* 2 3)',    6),
        ('(* 4 1)',    4),
        ('(/ 4 2)',    2),
        ('(/ 1 2)',    0.5),
        ('(// 1 2)',   0),
        ('(// 5 2)',   2),
        ('(** 2 3)',   8),
        ('(** 0 0)',   1),
        ('(sqrt 144)', 12),
        ('(sqrt 0)',   0),
        ('(sqrt 1)',   1),
        ('(! 0)',      1),
        ('(! 1)',      1),
        ('(! 4)',      24),
        ('(! 7)',      5040),
        ('(% 4 4)',    0),
        ('(% 5 6)',    5),
        ('(% 3 1)',    0),
    ]
    for source_code, expected_result in data:
        yield assert_equals, expected_result, limp.evaluate(source_code)


def test_comparison_functions_on_integers():
    data = [
        ('(> 1 0)',      True),
        ('(> 1 1)',      False),
        ('(> 0 1)',      False),
        ('(> 9999 321)', True),
        ('(> -10 -20)',  True),

        ('(>= 1 0)',      True),
        ('(>= 1 1)',      True),
        ('(>= 0 1)',      False),
        ('(>= 9999 321)', True),
        ('(>= -10 -20)',  True),
        
        ('(< 10 11)',    True),
        ('(< 11 11)',    False),
        ('(< 12 10)',    False),
        ('(< 100 4321)', True),
        ('(< -99 -12)',  True),

        ('(<= 10 11)',    True),
        ('(<= 11 11)',    True),
        ('(<= 12 10)',    False),
        ('(<= 100 4321)', True),
        ('(<= -99 -12)',  True),

        ('(= 9 9)', True),
        ('(= 4 5)', False),
        ('(= 1 1)', True),
    ]
    for source_code, expected_result in data:
        yield assert_equals, expected_result, limp.evaluate(source_code)
