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

    # Objects
    ('{}', (TT.Object, [])),

    ('{age: 10}', (TT.Object, [((TT.Symbol, 'age'), (TT.Integer, '10'))])),

    ('{name:"brandon" age:21}', (TT.Object,
                                 [((TT.Symbol, 'name'), (TT.String, '"brandon"')),
                                  ((TT.Symbol, 'age'), (TT.Integer, '21'))])),

    ('{colours: ["red" "green" "blue"]}', (TT.Object,
                                          [((TT.Symbol, 'colours'),
                                            (TT.List, [(TT.String, '"red"'),
                                                       (TT.String, '"green"'),
                                                       (TT.String, '"blue"')]))])),


    # Nested Objects
    ('{foo:{}}', (TT.Object,
                  [((TT.Symbol, 'foo'), (TT.Object, []))])),

    ('''
{
    name: "Blarg Smith"
    age: 1337
    interests: ["food" "limp" "THPS"]
    address: {
        house-number: 420
        street: "earth street"
    }
    job: "professional door knocker"
}
    ''',
     (TT.Object, [
         ((TT.Symbol, 'name'), (TT.String, '"Blarg Smith"')),
         ((TT.Symbol, 'age'), (TT.Integer, '1337')),
         ((TT.Symbol, 'interests'), (TT.List, [(TT.String, '"food"'),
                                               (TT.String, '"limp"'),
                                               (TT.String, '"THPS"')])),
         ((TT.Symbol, 'address'),
          (TT.Object,[
                  ((TT.Symbol, 'house-number'), (TT.Integer, '420')),
                  ((TT.Symbol, 'street'), (TT.String, '"earth street"'))
          ])),

         ((TT.Symbol, 'job'), (TT.String, '"professional door knocker"'))
     ])),

    ('person.name', (TT.AttributeAccess, (TT.Symbol, 'person'), (TT.Symbol, 'name'))),

    ('person.address.street', (TT.AttributeAccess,
                               (TT.AttributeAccess,
                                (TT.Symbol, 'person'),
                                (TT.Symbol, 'address')),
                               (TT.Symbol, 'street'))),

    ('thug-pro.players.byxor.skill-level', (TT.AttributeAccess,
                                            (TT.AttributeAccess,
                                             (TT.AttributeAccess,
                                              (TT.Symbol, 'thug-pro'),
                                              (TT.Symbol, 'players')),
                                             (TT.Symbol, 'byxor')),
                                            (TT.Symbol, 'skill-level'))),

    ('{name: "byxor"}.name', (TT.AttributeAccess,
                              (TT.Object,
                               [((TT.Symbol, 'name'),
                                 (TT.String, '"byxor"'))]),
                              (TT.Symbol, 'name'))),

    # Function Calls with Attribute Access
    ('(= [] {xyz:[]}.xyz)', (TT.FunctionCall,
                             (TT.Symbol, '='),
                             [(TT.List, []),
                              (TT.AttributeAccess,
                               (TT.Object,
                                [((TT.Symbol, 'xyz'),
                                  (TT.List, []))]),
                               (TT.Symbol, 'xyz'))])),

    # Conditionals
    ('if {true:10}', (TT.Conditional, [((TT.Boolean, 'true'), (TT.Integer, '10'))], None)),

    ('if {(= age 10): "ten"}', (TT.Conditional,
                                [((TT.FunctionCall,
                                   (TT.Symbol, '='),
                                   [(TT.Symbol, 'age'),
                                    (TT.Integer, '10')]),
                                  (TT.String, '"ten"'))],
                                None)),

    ('''
if {
  (= age 10): "ten"
  (= age 20): "twenty"
  (= age 30): "thirty"
}
''', (TT.Conditional,

      [((TT.FunctionCall,
         (TT.Symbol, '='),
         [(TT.Symbol, 'age'),
          (TT.Integer, '10')]),
        (TT.String, '"ten"')),

       ((TT.FunctionCall,
         (TT.Symbol, '='),
         [(TT.Symbol, 'age'),
          (TT.Integer, '20')]),
        (TT.String, '"twenty"')),

       ((TT.FunctionCall,
         (TT.Symbol, '='),
         [(TT.Symbol, 'age'),
          (TT.Integer, '30')]),
        (TT.String, '"thirty"'))],

      None)),
]


def test_creation_from_tokens():
    for source_code, expected_syntax_tree in data:
        print()
        print("---------------------------------------------")
        print(source_code)
        tokens = Tokens.create_from(source_code)
        syntax_tree = SyntaxTree.create_from(tokens)
        print()
        print("Actual:  ", syntax_tree)
        print("Expected:", expected_syntax_tree)
        yield assert_equals, expected_syntax_tree, syntax_tree
