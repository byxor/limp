import limp
import limp.environment as Environment
from unittest.mock import MagicMock
from nose.tools import assert_equals


def test_standard_library():
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

        # Integer equality function
        ('(= 9 9)', True),
        ('(= 4 5)', False),
        ('(= 1 1)', True),

        # String equality function
        ('(= "" "")',            True),
        ('(= "a" "a")',          True),
        ('(= "ab" "ab")',        True),
        ('(= "car" "avan")',     False),
        ('(= "tayne" "mayne")',  False),

        # Boolean equality function
        ('(= true false)',  False),
        ('(= false true)',  False),
        ('(= true true)',  True),
        ('(= false false)',  True),

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
        ('(string 0)',    "0"),

        ('(strip " x ")',                "x"),
        ('(strip " abc ")',              "abc"),
        ('(strip " x \t\n")',            "x"),
        ('(strip "hello \n\t\n there")', "hello \n\t\n there"),

        ('(length "")',      0),
        ('(length "a")',     1),
        ('(length "ab")',    2),
        ('(length "abc")',   3),
        ('(length "tayne")', 5),

        ('(in "" "")',                            True),
        ('(in "a" "a")',                          True),
        ('(in "abc" "abcde")',                    True),
        ('(in "bc" "abcde")',                     True),
        ('(in "car" "car is red")',               True),
        ('(in "a" "b")',                          False),
        ('(in "abacus" "b")',                     False),
        ('(in "self-respect" "php-programmers")', False),

        ('(repeat "" 10)',       ""),
        ('(repeat "a" 5)',       "aaaaa"),
        ('(repeat "hey " 3)',    "hey hey hey "),
        ('(repeat "racecar" 3)', "racecarracecarracecar"),

        ('(reverse "")',      ""),
        ('(reverse "abc")',   "cba"),
        ('(reverse "lol")',   "lol"),
        ('(reverse "jesus")', "susej"),

        ('(lowercase "abc")',       "abc"),
        ('(lowercase "AbC")',       "abc"),
        ('(lowercase "LIMP 2017")', "limp 2017"),
        ('(lowercase "Byxor")',     "byxor"),

        ('(uppercase "abc")',       "ABC"),
        ('(uppercase "AbC")',       "ABC"),
        ('(uppercase "LIMP 2017")', "LIMP 2017"),
        ('(uppercase "Byxor")',     "BYXOR"),

        # List functions
        ('(map (list 1 2 3) (function (n) (* n 2)))', [2, 4, 6]),
        ('(map (list 1 2 3) (function (n) (+ n 1)))', [2, 3, 4]),
        ('(map (list 10 20) (function (n) (/ n 2)))', [5, 10]),

        ('(filter (list 1 2 3 4) (function (n) (= (% n 2) 0)))', [2, 4]),
        ('(filter (list 1 2 3 4) (function (n) (= (% n 2) 1)))', [1, 3]),
        ('(filter (list 1 1 1 0) (function (n) (= n 1)))',       [1, 1, 1]),

        ('(element (list 0 1 2) 0)',       0),
        ('(element (list 0 1 2) 1)',       1),
        ('(element (list 0 1 2) 2)',       2),
        ('(element (list "foo" "bar") 0)', "foo"),
        ('(element (list "foo" "bar") 1)', "bar"),

        ('(append (list) 1)',                 [1]),
        ('(append (list "foo") 2)',           ["foo", 2]),
        ('(append (list "foo" "bar") "baz")', ["foo", "bar", "baz"]),

        ('(concatenate (list 0 1) (list 2 3))',  [0, 1, 2, 3]),
        ('(concatenate (list 0 1) 2 3 4 5 6 7)', [0, 1, 2, 3, 4, 5, 6, 7]),
        ('(concatenate (list true) false true)', [True, False, True]),
        
        ('(first (list "barry" "the" "blender"))', "barry"),
        ('(first (list "lazy" "game" "reviews"))', "lazy"),
        ('(first (list 8 "bit" "guy"))',           8),

        ('(last (list "barry" "the" "blender"))', "blender"),
        ('(last (list "lazy" "game" "reviews"))', "reviews"),
        ('(last (list 8 "bit" "guy"))',           "guy"),

        ('(all-but-first (list 1 2 3))', [2, 3]),
        ('(all-but-first (list 3 4 5))', [4, 5]),
        ('(all-but-first (list 5 6 7))', [6, 7]),

        ('(all-but-last (list 1 2 3))', [1, 2]),
        ('(all-but-last (list 3 4 5))', [3, 4]),
        ('(all-but-last (list 5 6 7))', [5, 6]),

        # Easter egg definitions
        ('bizkit', "Keep ROLLIN ROLLIN ROLLIN ROLLIN whaaat!"),
    ]
    for source_code, expected_result in data:
        yield (assert_equals, expected_result, limp.evaluate(source_code))


def test_looping_functions():
    FUNCTION_NAME = 'my_function'
    ARBITRARY_ITERATION_LIMIT = 100

    # test 'times' function
    for iterations in range(ARBITRARY_ITERATION_LIMIT):
        my_function = MagicMock()
        environment = Environment.create_standard()
        environment.define(FUNCTION_NAME, my_function)
        limp.evaluate(f'(times {iterations} {FUNCTION_NAME})', environment)
        yield assert_equals, iterations, my_function.call_count


    # test 'iterate' function
    my_function = MagicMock()
    environment = Environment.create_standard()
    environment.define(FUNCTION_NAME, my_function)
    limp.evaluate(f'(iterate {ARBITRARY_ITERATION_LIMIT} {FUNCTION_NAME})', environment)
    for i in range(iterations):
        yield my_function.assert_any_call, i
