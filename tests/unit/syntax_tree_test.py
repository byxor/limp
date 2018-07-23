from nose.tools import assert_equals
import limp.syntax_tree as SyntaxTree
import limp.tokens as Tokens


TreeTypes = SyntaxTree.Types


def test_creation_from_tokens():
    data = [
        ([], []),

        # Integers
        ('100', [(TreeTypes.Integer, '100')]),
        ('500', [(TreeTypes.Integer, '500')]),

        # Positive/Negative Integers
        ('+100', [(TreeTypes.UnaryPositive, (TreeTypes.Integer, '100'))]),
        ('-500', [(TreeTypes.UnaryNegative, (TreeTypes.Integer, '500'))]),

        # Floats
        ('0.123',  [(TreeTypes.Float, '0.123')]),
        ('.99',    [(TreeTypes.Float, '.99')]),
        
        # Positive/Negative Floats
        ('+99.8',  [(TreeTypes.UnaryPositive, (TreeTypes.Float, '99.8'))]),
        ('-0.123', [(TreeTypes.UnaryNegative, (TreeTypes.Float, '0.123'))]),

        # Hexadecimals
        ('0xDeaDa55',    [(TreeTypes.Hexadecimal, '0xDeaDa55')]),
        ('0xBEEF123aaa', [(TreeTypes.Hexadecimal, '0xBEEF123aaa')]),

        # Positive/Negative Hexadecimals
        ('+0xDeaDa55',    [(TreeTypes.UnaryPositive, (TreeTypes.Hexadecimal, '0xDeaDa55'))]),
        ('-0xBEEF123aaa', [(TreeTypes.UnaryNegative, (TreeTypes.Hexadecimal, '0xBEEF123aaa'))]),

        # Octals
        ('0o7654321', [(TreeTypes.Octal, '0o7654321')]),
        ('0o111',     [(TreeTypes.Octal, '0o111')]),

        # Positive/Negative Octals
        ('+0o7654321', [(TreeTypes.UnaryPositive, (TreeTypes.Octal, '0o7654321'))]),
        ('-0o111',     [(TreeTypes.UnaryNegative, (TreeTypes.Octal, '0o111'))]),

        # Binaries
        ('0b101010', [(TreeTypes.Binary, '0b101010')]),
        ('0b111110', [(TreeTypes.Binary, '0b111110')]),

        # Strings
        ('"hi()!"',           [(TreeTypes.String, '"hi()!"')]),
        ('"super string ->"', [(TreeTypes.String, '"super string ->"')]),

        # Function calls
        ("(destroy-evidence)", [(TreeTypes.FunctionCall, ("destroy-evidence"))]),
    ]

    for source_code, expected_syntax_tree in data:
        tokens = Tokens.create_from(source_code)
        syntax_tree = SyntaxTree.create_from(tokens)
        yield assert_equals, expected_syntax_tree, syntax_tree
