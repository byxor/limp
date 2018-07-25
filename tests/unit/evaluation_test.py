import limp.tokens as Tokens
import limp.syntax_tree as SyntaxTree
import limp.evaluation as Evaluation

from nose.tools import assert_equals


def test_evaluation():
    data = [
        # Numbers
        ('1',     1),
        ('2',     2),
        ('-10',   -10),
        ('-30',   -30),
        ('+1337', +1337),
        ('+9008', +9008),

        ('0b1010',      0b1010),
        ('0b11111111',  0b11111111),
        ('-0b1010',     -0b1010),
        ('-0b11111111', -0b11111111),
        ('+0b1010',     +0b1010),
        ('+0b11111111', +0b11111111),

        ('0o1234567',  0o1234567),
        ('0o0000000',  0o0),
        ('-0o1234567', -0o1234567),
        ('-0o0000000', -0o0),
        ('+0o1234567', +0o1234567),
        ('+0o0000000', +0o0),

        ('0xff',       0xff),
        ('0xBEEF',     0xBEEF),
        ('-0x13',      -0x13),
        ('-0xdeada55', -0xdeada55),
        ('+0x33333',   +0x33333),
        ('+0x444422',  +0x444422),

        # Strings
        ('""',          ""),
        ('"hi"',        "hi"),
        ('"hello!"',    "hello!"),
        ('"I <3 LIMP"', "I <3 LIMP"),
    ]
    for source_code, expected_result in data:
        tokens = Tokens.create_from(source_code)
        syntax_tree = SyntaxTree.create_from(tokens)
        result = Evaluation.evaluate(syntax_tree)
        yield assert_equals, expected_result, result
