import tests.helpers as Helpers


def test():
    Helpers.run_evaluation_test_on([
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
    ])
