import limp.errors as Errors
import limp.tokens as Tokens
from nose.tools import assert_equals, assert_raises


def test_creation_from_source_code():
    data = [
        ('1',                     [(Tokens.Types.Integer, '1')]),
        ('1003499',               [(Tokens.Types.Integer, '1003499')]),
        ('+123',                  [(Tokens.Types.Integer, '+123')]),
        ('-321',                  [(Tokens.Types.Integer, '-321')]),

        ('155.45',                [(Tokens.Types.Float, '155.45')]),
        ('.123',                  [(Tokens.Types.Float, '.123')]),
        ('+.123',                 [(Tokens.Types.Float, '+.123')]),
        ('-9.92',                 [(Tokens.Types.Float, '-9.92')]),

        ('0b11110',               [(Tokens.Types.Binary, '0b11110')]),
        ('+0b10',                 [(Tokens.Types.Binary, '+0b10')]),
        ('-0b001',                [(Tokens.Types.Binary, '-0b001')]),

        ('0o7654',                [(Tokens.Types.Octal, '0o7654')]),
        ('+0o224',                [(Tokens.Types.Octal, '+0o224')]),
        ('-0o125',                [(Tokens.Types.Octal, '-0o125')]),

        ('0xb3EeF',               [(Tokens.Types.Hexadecimal, '0xb3EeF')]),
        ('+0xdeAd',               [(Tokens.Types.Hexadecimal, '+0xdeAd')]),
        ('-0xa55',                [(Tokens.Types.Hexadecimal, '-0xa55')]),

        ('()',                    [(Tokens.Types.OpenParenthesis, '('),
                                   (Tokens.Types.CloseParenthesis, ')')]),

        ('(abc)',                 [(Tokens.Types.OpenParenthesis, '('),
                                   (Tokens.Types.Symbol, 'abc'),
                                   (Tokens.Types.CloseParenthesis, ')')]),

        ('(abc 0xdE 0b1 0o721)',  [(Tokens.Types.OpenParenthesis, '('),
                                   (Tokens.Types.Symbol, 'abc'),
                                   (Tokens.Types.Hexadecimal, '0xdE'),
                                   (Tokens.Types.Binary, '0b1'),
                                   (Tokens.Types.Octal, '0o721'),
                                   (Tokens.Types.CloseParenthesis, ')')]),

        ('(send "Hello there!")', [(Tokens.Types.OpenParenthesis, '('),
                                   (Tokens.Types.Symbol, 'send'),
                                   (Tokens.Types.String, '"Hello there!"'),
                                   (Tokens.Types.CloseParenthesis, ')')]),

        ('(display "0   4")',     [(Tokens.Types.OpenParenthesis, '('),
                                   (Tokens.Types.Symbol, 'display'),
                                   (Tokens.Types.String, '"0   4"'),
                                   (Tokens.Types.CloseParenthesis, ')')]),

        ('(reverse "(abc)")',     [(Tokens.Types.OpenParenthesis, '('),
                                   (Tokens.Types.Symbol, 'reverse'),
                                   (Tokens.Types.String, '"(abc)"'),
                                   (Tokens.Types.CloseParenthesis, ')')]),
    ]
    for source_code, expected_tokens in data:
        tokens = Tokens.create_from(source_code)
        yield assert_equals, expected_tokens, tokens


# def test_exception_raised_if_code_is_empty():
#     data = ["", " ", "\n", "   \n\t"]
#     for source_code in data:
#         yield assert_raises, Errors.EmptyCode, Tokens.create_from, source_code


# def test_exception_raised_if_too_many_closing_parentheses():
#     data = ['())', ')', '(foo) )    ']
#     for source_code in data:
#         yield (assert_raises, Errors.ExtraClosingParenthesis,
#                Tokens.create_from, source_code)


# def test_exception_raised_if_too_few_closing_parentheses():
#     data = ['(', '((', '(()']
#     for source_code in data:
#         yield (assert_raises, Errors.MissingClosingParenthesis,
#                Tokens.create_from, source_code)
