import limp.tokens as Tokens
from nose.tools import assert_equals


def test_creation_from_source_code():
    data = [
        ('false', [(Tokens.Types.Boolean, 'false')]),
        ('true',  [(Tokens.Types.Boolean, 'true')]),

        ('falses',  [(Tokens.Types.Symbol, 'falses')]),
        ('trues',   [(Tokens.Types.Symbol, 'trues')]),
        ('unfalse', [(Tokens.Types.Symbol, 'unfalse')]),
        ('untrue',  [(Tokens.Types.Symbol, 'untrue')]),

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

        ('(n -> (+ n 1))',        [(Tokens.Types.OpenParenthesis, '('),
                                   (Tokens.Types.Symbol, 'n'),
                                   (Tokens.Types.FunctionDelimiter, '->'),
                                   (Tokens.Types.OpenParenthesis, '('),
                                   (Tokens.Types.Symbol, '+'),
                                   (Tokens.Types.Symbol, 'n'),
                                   (Tokens.Types.Integer, '1'),
                                   (Tokens.Types.CloseParenthesis, ')'),
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

        ('[]', [(Tokens.Types.OpenSquareBracket, '['),
                (Tokens.Types.CloseSquareBracket, ']')]),

        ('[1 2 3]', [(Tokens.Types.OpenSquareBracket, '['),
                     (Tokens.Types.Integer, '1'),
                     (Tokens.Types.Integer, '2'),
                     (Tokens.Types.Integer, '3'),
                     (Tokens.Types.CloseSquareBracket, ']')]),

        ('{}', [(Tokens.Types.OpenCurlyBrace, '{'),
                (Tokens.Types.CloseCurlyBrace, '}')]),

        ('{age: 10}', [(Tokens.Types.OpenCurlyBrace, '{'),
                       (Tokens.Types.Symbol, 'age'),
                       (Tokens.Types.ObjectDelimiter, ':'),
                       (Tokens.Types.Integer, '10'),
                       (Tokens.Types.CloseCurlyBrace, '}')]),

        ('person.name', [(Tokens.Types.Symbol, 'person'),
                         (Tokens.Types.AttributeAccessDelimiter, '.'),
                         (Tokens.Types.Symbol, 'name')]),

        ('person.address.street', [(Tokens.Types.Symbol, 'person'),
                                   (Tokens.Types.AttributeAccessDelimiter, '.'),
                                   (Tokens.Types.Symbol, 'address'),
                                   (Tokens.Types.AttributeAccessDelimiter, '.'),
                                   (Tokens.Types.Symbol, 'street')]),
    ]
    for source_code, expected_tokens in data:
        tokens = Tokens.create_from(source_code)
        print("-------------")
        print(tokens)
        print(expected_tokens)
        yield assert_equals, expected_tokens, tokens
