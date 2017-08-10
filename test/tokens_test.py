import limp.tokens as tokens


def test_creation_from_source_code():
    data = [
        ('()', ['(', ')']),
        ('(abc)', ['(', 'abc', ')']),
        ('(abc 1 2 3)', ['(', 'abc', '1', '2', '3', ')'])
    ]
    for source_code, expected_tokens in data:
        assert tokens.create_from(source_code) == expected_tokens
