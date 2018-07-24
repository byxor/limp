from nose.tools import assert_equals
import limp.syntax_tree as SyntaxTree
import limp.tokens as Tokens


TreeTypes = SyntaxTree.Types


def test_creation_from_tokens():
    data = [
        ([], []),

        # Integers
        ('100', (TreeTypes.Integer, '100')),
        ('500', (TreeTypes.Integer, '500')),

        # Positive/Negative Integers
        ('+100', (TreeTypes.UnaryPositive, (TreeTypes.Integer, '100'))),
        ('-500', (TreeTypes.UnaryNegative, (TreeTypes.Integer, '500'))),

        # Floats
        ('0.123',  (TreeTypes.Float, '0.123')),
        ('.99',    (TreeTypes.Float, '.99')),
        
        # Positive/Negative Floats
        ('+99.8',  (TreeTypes.UnaryPositive, (TreeTypes.Float, '99.8'))),
        ('-0.123', (TreeTypes.UnaryNegative, (TreeTypes.Float, '0.123'))),

        # Hexadecimals
        ('0xDeaDa55',    (TreeTypes.Hexadecimal, '0xDeaDa55')),
        ('0xBEEF123aaa', (TreeTypes.Hexadecimal, '0xBEEF123aaa')),

        # Positive/Negative Hexadecimals
        ('+0xDeaDa55',    (TreeTypes.UnaryPositive, (TreeTypes.Hexadecimal, '0xDeaDa55'))),
        ('-0xBEEF123aaa', (TreeTypes.UnaryNegative, (TreeTypes.Hexadecimal, '0xBEEF123aaa'))),

        # Octals
        ('0o7654321', (TreeTypes.Octal, '0o7654321')),
        ('0o111',     (TreeTypes.Octal, '0o111')),

        # Positive/Negative Octals
        ('+0o7654321', (TreeTypes.UnaryPositive, (TreeTypes.Octal, '0o7654321'))),
        ('-0o111',     (TreeTypes.UnaryNegative, (TreeTypes.Octal, '0o111'))),

        # Binaries
        ('0b101010', (TreeTypes.Binary, '0b101010')),
        ('0b111110', (TreeTypes.Binary, '0b111110')),

        # Strings
        ('"hi()!"',           (TreeTypes.String, '"hi()!"')),
        ('"super string ->"', (TreeTypes.String, '"super string ->"')),

        # Function calls
        ('(fibonacci)', (TreeTypes.FunctionCall,
                         [(TreeTypes.Symbol, 'fibonacci')])),

        ('(destroy-evidence)', (TreeTypes.FunctionCall,
                                [(TreeTypes.Symbol, 'destroy-evidence')])),

        ('(steal-cookies 99)', (TreeTypes.FunctionCall,
                                [(TreeTypes.Symbol, 'steal-cookies'),
                                 (TreeTypes.Integer, '99')])),


        ('(steal-biscuits 22)', (TreeTypes.FunctionCall,
                                 [(TreeTypes.Symbol, 'steal-biscuits'),
                                  (TreeTypes.Integer, '22')])),

        ('(reverse "foo")', (TreeTypes.FunctionCall,
                             [(TreeTypes.Symbol, 'reverse'),
                              (TreeTypes.String, '"foo"')])),

        ('(+ 1 2)', (TreeTypes.FunctionCall,
                     [(TreeTypes.Symbol, '+'),
                      (TreeTypes.Integer, '1'),
                      (TreeTypes.Integer, '2')])),

        ('(concatenate "foo" "bar" "baz")', (TreeTypes.FunctionCall,
                                             [(TreeTypes.Symbol, 'concatenate'),
                                              (TreeTypes.String, '"foo"'),
                                              (TreeTypes.String, '"bar"'),
                                              (TreeTypes.String, '"baz"')])),

        ('(f (g))', (TreeTypes.FunctionCall,
                     [(TreeTypes.Symbol, 'f'),
                      (TreeTypes.FunctionCall,
                       [(TreeTypes.Symbol, 'g')])])),

        ('(+ 10 (- 100 50))', (TreeTypes.FunctionCall,
                               [(TreeTypes.Symbol, '+'),
                                (TreeTypes.Integer, '10'),
                                (TreeTypes.FunctionCall,
                                 [(TreeTypes.Symbol, '-'),
                                  (TreeTypes.Integer, '100'),
                                  (TreeTypes.Integer, '50')])])),
    ]

    for source_code, expected_syntax_tree in data:
        print("\n\n------------------")

        tokens = Tokens.create_from(source_code)

        print("Tokens:  ", tokens)
        print("Expected:", expected_syntax_tree)


        syntax_tree = SyntaxTree.create_from(tokens)

        print("Actual:  ", syntax_tree)

        yield assert_equals, expected_syntax_tree, syntax_tree
