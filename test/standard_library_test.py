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
        ('(% 3 1)',    0)
    ]
    for source_code, expected_result in data:
        yield assert_equals, expected_result, limp.evaluate(source_code)
