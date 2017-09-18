import limp.tokens as Tokens
from nose.tools import assert_equals


def test_creation_from_source_code():
    data = [
        ('()',          ['(', ')']),
        ('(abc)',       ['(', 'abc', ')']),
        ('(abc 1 2 3)', ['(', 'abc', '1', '2', '3', ')'])
    ]
    for source_code, expected_tokens in data:
        tokens = Tokens.create_from(source_code)
        yield assert_equals, expected_tokens, tokens
