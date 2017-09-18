import limp.tokens as Tokens
from nose.tools import assert_equals


def test_creation_from_source_code():
    data = [
        ('1',                     ['1']),
        ('()',                    ['(', ')']),
        ('(abc)',                 ['(', 'abc', ')']),
        ('(abc 1 2 3)',           ['(', 'abc', '1', '2', '3', ')']),
        ('(send "Hello there!")', ['(', 'send', '"Hello there!"', ')']),
        ('(display "0   4")',     ['(', 'display', '"0   4"', ')']),
    ]
    for source_code, expected_tokens in data:
        tokens = Tokens.create_from(source_code)
        yield assert_equals, expected_tokens, tokens
