import limp
import limp.environment as Environment
from unittest.mock import MagicMock
from nose.tools import assert_equals


def test_standard_library():
    data = [
        # Easter egg definitions
        ('bizkit', "Keep ROLLIN ROLLIN ROLLIN ROLLIN whaaat!"),
        
        # Mathematical functions
        ('(+ 1 1)',     2),
        ('(+ 2 3)',     5),
        ('(+ 1 2 3)',   6),
        ('(- 1 1)',     0),
        ('(- 4 2)',     2),
        ('(- 9 8 7)',   -6),
        ('(* 2 3)',     6),
        ('(* 4 1)',     4),
        ('(* 2 3 4)',   24),
        ('(/ 4 2)',     2),
        ('(/ 1 2)',     0.5),
        ('(/ 1 2 3)',   ((1 / 2) / 3)),
        ('(// 1 2)',    0),
        ('(// 5 2)',    2),
        ('(// 99 2 2)', ((99 // 2) // 2)),
        ('(** 2 3)',    8),
        ('(** 0 0)',    1),
        ('(sqrt 144)',  12),
        ('(sqrt 0)',    0),
        ('(sqrt 1)',    1),
        ('(! 0)',       1),
        ('(! 1)',       1),
        ('(! 4)',       24),
        ('(! 7)',       5040),
        ('(% 4 4)',     0),
        ('(% 5 6)',     5),
        ('(% 3 1)',     0),
        
        ('(divisor? 3 9)',   True),
        ('(divisor? 3 99)',  True),
        ('(divisor? 2 44)',  True),
        ('(divisor? 2 45)',  False),
        ('(divisor? 44 45)', False),

        ('(even? 0)', True),
        ('(even? 1)', False),
        ('(even? 2)', True),
        ('(even? 3)', False),
        ('(even? 4)', True),
        ('(even? 5)', False),

        ('(odd? 0)', False),
        ('(odd? 1)', True),
        ('(odd? 2)', False),
        ('(odd? 3)', True),
        ('(odd? 4)', False),
        ('(odd? 5)', True),

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

        ('(strip " x ")',                "x"),
        ('(strip " abc ")',              "abc"),
        ('(strip " x \t\n")',            "x"),
        ('(strip "hello \n\t\n there")', "hello \n\t\n there"),

        ('(length "")',      0),
        ('(length "a")',     1),
        ('(length "ab")',    2),
        ('(length "abc")',   3),
        ('(length "tayne")', 5),

        ('(in? "" "")',                            True),
        ('(in? "a" "a")',                          True),
        ('(in? "abc" "abcde")',                    True),
        ('(in? "bc" "abcde")',                     True),
        ('(in? "car" "car is red")',               True),
        ('(in? "a" "b")',                          False),
        ('(in? "abacus" "b")',                     False),
        ('(in? "self-respect" "php-programmers")', False),

        ('(empty? "")',       True),
        ('(empty? ".")',      False),
        ('(empty? "hello!")', False),

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

        ('(split " " "a b c")',             ['a', 'b', 'c']),
        ('(split " " "ruby   81")',         ['ruby', '', '', '81']),
        ('(split ", " "test, 1, 2, 3")',    ['test', '1', '2', '3']),
        ('(split ", " "cars, the, movie")', ['cars', 'the', 'movie']),

        ('(join-string " " (list "1" "2" "3"))',        "1 2 3"),
        ('(join-string " " (list "4" "5" "6"))',        "4 5 6"),
        ('(join-string "_::_" (list "tayne" "brain"))', "tayne_::_brain"),

        # List functions
        ('(map (function (n) (* n 2)) (list 1 2 3))', [2, 4, 6]),
        ('(map (function (n) (+ n 1)) (list 1 2 3))', [2, 3, 4]),
        ('(map (function (n) (/ n 2)) (list 10 20))', [5, 10]),

        ('(filter (function (n) (= (% n 2) 0)) (list 1 2 3 4))', [2, 4]),
        ('(filter (function (n) (= (% n 2) 1)) (list 1 2 3 4))', [1, 3]),
        ('(filter (function (n) (= n 1)) (list 1 1 1 0))',       [1, 1, 1]),

        ('(reduce + (list 1 2 3 4))', 10),
        ('(reduce - (list 1 2 3 4))', -8),
        ('(reduce + (list 9 10 11))', 30),

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

        # Conversion functions
        ('(string 123)', "123"),
        ('(string 999)', "999"),
        ('(string 0)',   "0"),

        ('(integer "32")', 32),
        ('(integer "-1")', -1),

        ('(float "4.2")',  4.2),
        ('(float "97.4")', 97.4),

        ('(boolean "false")', False),
        ('(boolean "true")',  True),

        # Curry function
        ('((curry + 10) 20)',     30),
        ('((curry + 10 1 2) 20)', 33),
        
        ('((curry map (function (n) (* n 2))) (list 1 2 3))', [2, 4, 6]),
        ('((curry filter (function (n) (= n 1))) (list 1 2 3))', [1]),
        
        # Chain function
        ("""(chain 0
              (function (n) (+ n 10))
              (function (n) (// n 2))
              string)""", "5"),

        ("""
          (chain (list 1 2 3 4 5 6 7 8 9 10)
            (curry map    (function (n) (* n 2)))
            (curry map    (function (n) (+ n 1)))
            (curry map    (function (n) (- n 1)))
            (curry filter (function (n) (= (% n 4) 0)))
            (curry reduce +))
         """, 60),

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