import limp
from nose.tools import assert_equals


def test_mathematical_functions():
    data = [
        
        # Mathematical functions
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

        # Comparison functions on integers             
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

        # Boolean functions
        ('(not true)',        False),
        ('(not false)',       True),
        ('(not (not true))',  True),
        ('(not (not false))', False),

        ('(and true true)',   True),
        ('(and true false)',  False),
        ('(and false true)',  False),
        ('(and false false)', False),

        ('(or true true)',   True),
        ('(or true false)',  True),
        ('(or false true)',  True),
        ('(or false false)', False),

        ('(xor true true)',   False),
        ('(xor true false)',  True),
        ('(xor false true)',  True),
        ('(xor false false)', False),

        # String functions
        ('(concatenate "foo" "bar")',      "foobar"),
        ('(concatenate "hello" " there")', "hello there"),
        ('(concatenate "a" "b" "c" "d")',  "abcd"),
        ('(concatenate "x" "y" "z" "?")',  "xyz?"),

        ('(string 123)',  "123"),
        ('(string 999)',  "999"),
    ]
    
    for source_code, expected_result in data:
        yield (assert_equals, expected_result, limp.evaluate(source_code))
