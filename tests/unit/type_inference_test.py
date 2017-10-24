import limp.types as Types
import tests.helpers as Helpers
from nose.tools import assert_equals
from tests.syntax import *


def test_type_inference():
    data = [
        (symbol('abc'),              Types.Symbol),
        (symbol('def'),              Types.Symbol),
        (integer(123),               Types.Integer),
        (integer(456),               Types.Integer),
        (positive(integer(2)),       Types.Integer),
        (negative(integer(1)),       Types.Integer),
        (float_(1.2),                Types.Float),
        (float_(2.4),                Types.Float),
        (positive(float_(0.2)),      Types.Float),
        (negative(float_(0.2)),      Types.Float),
        (hexadecimal(0x5),           Types.Hexadecimal),
        (hexadecimal(0xABC),         Types.Hexadecimal),
        (negative(hexadecimal(0x9)), Types.Hexadecimal),
        (negative(hexadecimal(0x1)), Types.Hexadecimal),
        (binary(0b1),                Types.Binary),
        (binary(0b101011),           Types.Binary),
        (positive(binary(0b1)),      Types.Binary),
        (negative(binary(0b0)),      Types.Binary),

        (boolean(True),         Types.Boolean),
        (boolean(False),        Types.Boolean),
        (string("Github!"),     Types.String),
        (string("Hello there"), Types.String),
        
        ([Types.Definition.KEYWORD, symbol('x'), integer(10)], Types.Definition),
        ([Types.Definition.KEYWORD, symbol('y'), integer(20)], Types.Definition),
        ([symbol('+'), integer(0), integer(1)],                Types.Invocation),
        ([symbol('return10')],                                 Types.Invocation),
        ([Types.SequentialEvaluator.KEYWORD],                  Types.SequentialEvaluator),
        
        ([Types.SequentialEvaluator.KEYWORD,
          symbol('x'), symbol('y'), symbol('z')],              Types.SequentialEvaluator),
        
        ([Types.SimpleConditional.KEYWORD,
          boolean(True), symbol('x')],                         Types.SimpleConditional),
        ([Types.SimpleConditional.KEYWORD,
          boolean(False), symbol('y')],                        Types.SimpleConditional),
        
        ([Types.ComplexConditional.KEYWORD,
          [boolean(True), string("bar")]],                     Types.ComplexConditional),
        
        ([Types.ComplexConditional.KEYWORD,
          [boolean(False), string("bar")],
          [boolean(True), string("baz")]],                     Types.ComplexConditional),
        
        ([Types.Function.KEYWORD, [], integer(0)],             Types.Function),
        
        ([Types.Function.KEYWORD, [symbol('x'), symbol('y')],
          [symbol('+'), symbol('x'), symbol('y')]],            Types.Function),

        ([Types.List.KEYWORD,
          symbol('x'), symbol('y'), symbol('z')],              Types.List),
        
        ([Types.List.KEYWORD, integer(100), integer(200)],     Types.List),
    ]
    for contents, expected_type in data:
        form = Types.Form.infer_from(contents, Helpers.sample_environment())
        yield assert_equals, expected_type, type(form)
