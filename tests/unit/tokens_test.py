import limp.errors as Errors
import limp.tokens as Tokens
from nose.tools import assert_equals, assert_raises


def test_creation_from_source_code():
    data = [
        ('1',                     ['1']),
        ('()',                    ['(', ')']),
        ('(abc)',                 ['(', 'abc', ')']),
        ('(abc 1 2 3)',           ['(', 'abc', '1', '2', '3', ')']),
        ('(send "Hello there!")', ['(', 'send', '"Hello there!"', ')']),
        ('(display "0   4")',     ['(', 'display', '"0   4"', ')']),
        ('(reverse "(abc)")',     ['(', 'reverse', '"(abc)"', ')']), 
    ]
    for source_code, expected_tokens in data:
        tokens = Tokens.create_from(source_code)
        yield assert_equals, expected_tokens, tokens


def test_exception_raised_if_code_is_empty():
    data = ["", " ", "\n", "   \n\t"]
    for source_code in data:
        yield assert_raises, Errors.EmptyCode, Tokens.create_from, source_code


def test_exception_raised_if_too_many_closing_parentheses():
    data = ['())', ')', '(foo) )    ']
    for source_code in data:
        yield (assert_raises, Errors.ExtraClosingParenthesis,
               Tokens.create_from, source_code)


def test_exception_raised_if_too_few_closing_parentheses():
    data = ['(', '((', '(()']
    for source_code in data:
        yield (assert_raises, Errors.MissingClosingParenthesis,
               Tokens.create_from, source_code)
