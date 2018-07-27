import limp.syntax_tree as SyntaxTree
import limp.tokens as Tokens
from nose.tools import assert_equals


TT = SyntaxTree.Types


data = [
    ([], None),

    # Booleans
    ('true',  (TT.Boolean, 'true')),
    ('false', (TT.Boolean, 'false')),

    # Integers
    ('100', (TT.Integer, '100')),
    ('500', (TT.Integer, '500')),

    # Positive/Negative Integers
    ('+100', (TT.UnaryPositive, (TT.Integer, '100'))),
    ('-500', (TT.UnaryNegative, (TT.Integer, '500'))),

    # Floats
    ('0.123', (TT.Float, '0.123')),
    ('.99',   (TT.Float, '.99')),

    # Positive/Negative Floats
    ('+99.8',  (TT.UnaryPositive, (TT.Float, '99.8'))),
    ('-0.123', (TT.UnaryNegative, (TT.Float, '0.123'))),

    # Hexadecimals
    ('0xDeaDa55',    (TT.Hexadecimal, '0xDeaDa55')),
    ('0xBEEF123aaa', (TT.Hexadecimal, '0xBEEF123aaa')),

    # Positive/Negative Hexadecimals
    ('+0xDeaDa55',    (TT.UnaryPositive, (TT.Hexadecimal, '0xDeaDa55'))),
    ('-0xBEEF123aaa', (TT.UnaryNegative, (TT.Hexadecimal, '0xBEEF123aaa'))),

    # Octals
    ('0o7654321', (TT.Octal, '0o7654321')),
    ('0o111',     (TT.Octal, '0o111')),

    # Positive/Negative Octals
    ('+0o7654321', (TT.UnaryPositive, (TT.Octal, '0o7654321'))),
    ('-0o111',     (TT.UnaryNegative, (TT.Octal, '0o111'))),

    # Binaries
    ('0b101010', (TT.Binary, '0b101010')),
    ('0b111110', (TT.Binary, '0b111110')),

    # Positive/Negative Binaries
    ('+0b101010', (TT.UnaryPositive, (TT.Binary, '0b101010'))),
    ('-0b111110', (TT.UnaryNegative, (TT.Binary, '0b111110'))),

    # Strings
    ('"hi()!"',           (TT.String, '"hi()!"')),
    ('"super string ->"', (TT.String, '"super string ->"')),

    # Symbols
    ('name',       (TT.Symbol, 'name')),
    ('my-address', (TT.Symbol, 'my-address')),

    # Function Calls
    ('(fibonacci)', (TT.FunctionCall, (TT.Symbol, 'fibonacci'), [])),

    ('(destroy-evidence)', (TT.FunctionCall, (TT.Symbol, 'destroy-evidence'), [])),

    ('(steal-cookies 99)', (TT.FunctionCall, (TT.Symbol, 'steal-cookies'),
                            [(TT.Integer, '99')])),


    ('(steal-biscuits 22)', (TT.FunctionCall, (TT.Symbol, 'steal-biscuits'),
                             [(TT.Integer, '22')])),

    ('(reverse "foo")', (TT.FunctionCall, (TT.Symbol, 'reverse'),
                         [(TT.String, '"foo"')])),

    ('(+ 1 2)', (TT.FunctionCall, (TT.Symbol, '+'),
                 [(TT.Integer, '1'),
                  (TT.Integer, '2')])),

    ('(concatenate "foo" "bar" "baz")', (TT.FunctionCall,
                                         (TT.Symbol, 'concatenate'),
                                         [(TT.String, '"foo"'),
                                          (TT.String, '"bar"'),
                                          (TT.String, '"baz"')])),

    ('(f (g))', (TT.FunctionCall,
                 (TT.Symbol, 'f'),
                 [(TT.FunctionCall,
                   (TT.Symbol, 'g'),
                   [])])),

    ('(+ 10 (- 100 50))', (TT.FunctionCall,
                           (TT.Symbol, '+'),
                           [(TT.Integer, '10'),
                            (TT.FunctionCall,
                             (TT.Symbol, '-'),
                             [(TT.Integer, '100'),
                              (TT.Integer, '50')])])),

    ('(* (- 10 5) 2)', (TT.FunctionCall, (TT.Symbol, '*'),
                        [(TT.FunctionCall, (TT.Symbol, '-'),
                          [(TT.Integer, '10'),
                           (TT.Integer, '5')]),
                         (TT.Integer, '2')])),

    ('(* (- 10 (+ 1 1)) 2)', (TT.FunctionCall, (TT.Symbol, '*'),
                              [(TT.FunctionCall, (TT.Symbol, '-'),
                                [(TT.Integer, '10'),
                                 (TT.FunctionCall, (TT.Symbol, '+'),
                                  [(TT.Integer, '1'),
                                   (TT.Integer, '1')])]),
                               (TT.Integer, '2')])),

    ('(+ (- 1 2) (/ 3 4))',
     (TT.FunctionCall,
      (TT.Symbol, '+'),
      [(TT.FunctionCall,
        (TT.Symbol, '-'),
        [(TT.Integer, '1'),
         (TT.Integer, '2')]),
       (TT.FunctionCall,
        (TT.Symbol, '/'),
        [(TT.Integer, '3'),
         (TT.Integer, '4')])])),

    # Lists
    ('[]',    (TT.List, [])),
    ('[1]',   (TT.List, [(TT.Integer, '1')])),
    ('[(a)]', (TT.List, [(TT.FunctionCall, (TT.Symbol, 'a'), [])])),
    ('[1 2]', (TT.List, [(TT.Integer, '1'), (TT.Integer, '2')])),

    ('["uncle" "bob" "rules"]', (TT.List,
                                 [(TT.String, '"uncle"'),
                                  (TT.String, '"bob"'),
                                  (TT.String, '"rules"')])),

    ('[(+ 1 2)]', (TT.List,
                   [(TT.FunctionCall,
                     (TT.Symbol, '+'),
                     [(TT.Integer, '1'),
                      (TT.Integer, '2')])])),

    ('[(+ 1 2) (- 3 4)]', (TT.List,
                           [(TT.FunctionCall,
                             (TT.Symbol, '+'),
                             [(TT.Integer, '1'),
                              (TT.Integer, '2')]),
                            (TT.FunctionCall,
                             (TT.Symbol, '-'),
                             [(TT.Integer, '3'),
                              (TT.Integer, '4')])])),

    ('[[]]', (TT.List, [(TT.List, [])])),

    ('[[] []]', (TT.List,
                 [(TT.List, []),
                  (TT.List, [])])),

    ('[[1]]', (TT.List, [(TT.List, [(TT.Integer, '1')])])),

    ('[[1 2]]', (TT.List,
                 [(TT.List,
                   [(TT.Integer, '1'),
                    (TT.Integer, '2')])])),

    ('[[1] [2]]', (TT.List,
                   [(TT.List, [(TT.Integer, '1')]),
                    (TT.List, [(TT.Integer, '2')])])),


    ('[[1] [2 3]]', (TT.List,
                     [(TT.List,
                       [(TT.Integer, '1')]),
                      (TT.List,
                       [(TT.Integer, '2'),
                        (TT.Integer, '3')])])),

    ('[[(+ 0 1)] [2 3]]', (TT.List,
                           [(TT.List,
                             [(TT.FunctionCall,
                               (TT.Symbol, '+'),
                               [(TT.Integer, '0'),
                                (TT.Integer, '1')])]),
                            (TT.List,
                             [(TT.Integer, '2'),
                              (TT.Integer, '3')])])),

    # Function Calls with Lists
    ('(reverse [1 2])', (TT.FunctionCall,
                         (TT.Symbol, 'reverse'),
                         [(TT.List,
                           [(TT.Integer, '1'),
                            (TT.Integer, '2')])])),

    ('(reverse [[a] [b]])', (TT.FunctionCall,
                             (TT.Symbol, 'reverse'),
                             [(TT.List,
                               [(TT.List,
                                 [(TT.Symbol, 'a')]),
                                (TT.List,
                                 [(TT.Symbol, 'b')])])])),

    # Anonymous Functions
    ('(->10)', (TT.Function, [], (TT.Integer, '10'))),
    ('(->20)', (TT.Function, [], (TT.Integer, '20'))),

    ('(->(foo))', (TT.Function, [],
                   (TT.FunctionCall, (TT.Symbol, 'foo'), []))),

    ('(->(+ 0x9 0x10))', (TT.Function, [],
                          (TT.FunctionCall,
                           (TT.Symbol, '+'),
                           [(TT.Hexadecimal, '0x9'),
                            (TT.Hexadecimal, '0x10')]))),

    ('(n -> n)', (TT.Function, [(TT.Symbol, 'n')], (TT.Symbol, 'n'))),

    ('(a b -> (+ a b))', (TT.Function,
                          [(TT.Symbol, 'a'),
                           (TT.Symbol, 'b')],
                          (TT.FunctionCall,
                           (TT.Symbol, '+'),
                           [(TT.Symbol, 'a'),
                            (TT.Symbol, 'b')]))),

    # Nested Anonymous Functions
    ('(->(->1))', (TT.Function,
                   [],
                   (TT.Function,
                    [],
                    (TT.Integer, '1')))),

    ('(-> (-> (x -> (+ x 2))))', (TT.Function,
                                  [],
                                  (TT.Function,
                                   [],
                                   (TT.Function,
                                    [(TT.Symbol, 'x')],
                                    (TT.FunctionCall,
                                     (TT.Symbol, '+'),
                                     [(TT.Symbol, 'x'),
                                      (TT.Integer, '2')]))))),

    # Calling Anonymous Functions
    ('((->"hi"))', (TT.FunctionCall,
                    (TT.Function,
                     [],
                     (TT.String, '"hi"')),
                    [])),

    ('((n -> n) 5)', (TT.FunctionCall,
                      (TT.Function,
                       [(TT.Symbol, 'n')],
                       (TT.Symbol, 'n')),
                      [(TT.Integer, '5')])),

    ('((n -> (square-root n)) 16)', (TT.FunctionCall,
                                     (TT.Function,
                                      [(TT.Symbol, 'n')],
                                      (TT.FunctionCall,
                                       (TT.Symbol, 'square-root'),
                                       [(TT.Symbol, 'n')])),
                                     [(TT.Integer, '16')])),

    ('((list -> (reverse list)) ["foo" "bar"])', (TT.FunctionCall,
                                                  (TT.Function,
                                                   [(TT.Symbol, 'list')],
                                                   (TT.FunctionCall,
                                                    (TT.Symbol, 'reverse'),
                                                    [(TT.Symbol, 'list')])),
                                                  [(TT.List,
                                                    [(TT.String, '"foo"'),
                                                     (TT.String, '"bar"')])])),

    # If Statements
    ('(if true 10)', (TT.IfStatement, (TT.Boolean, 'true'), (TT.Integer, '10'), None)),

    ('(if true 10 20)', (TT.IfStatement,
                         (TT.Boolean, 'true'),
                         (TT.Integer, '10'),
                         (TT.Integer, '20'))),

    ('(if (not true) "foo" "bar")', (TT.IfStatement,
                                     (TT.FunctionCall,
                                      (TT.Symbol, 'not'),
                                      [(TT.Boolean, 'true')]),
                                     (TT.String, '"foo"'),
                                     (TT.String, '"bar"'))),

    ('(if (= 0b0 0b1) (+ 1 2) (->30))', (TT.IfStatement,
                                         (TT.FunctionCall,
                                          (TT.Symbol, '='),
                                          [(TT.Binary, '0b0'),
                                           (TT.Binary, '0b1')]),
                                         (TT.FunctionCall,
                                          (TT.Symbol, '+'),
                                          [(TT.Integer, '1'),
                                           (TT.Integer, '2')]),
                                         (TT.Function,
                                          [],
                                          (TT.Integer, '30')))),

    # Objects
    ('{}', (TT.Object, [])),

    ('{age: 10}', (TT.Object, [[(TT.Symbol, 'age'), (TT.Integer, '10')]])),
]


def test_creation_from_tokens():
    for source_code, expected_syntax_tree in data:
        print()
        print("-------------")
        print(source_code)
        tokens = Tokens.create_from(source_code)
        syntax_tree = SyntaxTree.create_from(tokens)
        # print(syntax_tree)
        # print(expected_syntax_tree)
        yield assert_equals, expected_syntax_tree, syntax_tree
