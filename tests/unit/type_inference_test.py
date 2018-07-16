
import limp.types as Types
import tests.helpers as Helpers
from nose.tools import assert_equals
from tests.syntax import *


def test_type_inference():
    data = [
        ('abc',              Types.Symbol),
        ('def',              Types.Symbol),

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

        (octal(0o1),                 Types.Octal),
        (octal(0o142423),            Types.Octal),
        (positive(octal(0o4234)),    Types.Octal),
        (negative(octal(0o3435)),    Types.Octal),

        (boolean(True),         Types.Boolean),
        (boolean(False),        Types.Boolean),

        (string("Github!"),     Types.String),
        (string("Hello there"), Types.String),

        ([Types.Definition.KEYWORD, 'x', integer(10)], Types.Definition),
        ([Types.Definition.KEYWORD, 'y', integer(20)], Types.Definition),

        (['+', integer(0), integer(1)], Types.Invocation),
        (['return10'],                  Types.Invocation),

        ([Types.SequentialEvaluator.KEYWORD, 'a', 'b'],      Types.SequentialEvaluator),
        ([Types.SequentialEvaluator.KEYWORD, 'x', 'y', 'z'], Types.SequentialEvaluator),

        ([Types.SimpleConditional.KEYWORD, boolean(True), 'x'],  Types.SimpleConditional),
        ([Types.SimpleConditional.KEYWORD, boolean(False), 'y'], Types.SimpleConditional),

        ([Types.ComplexConditional.KEYWORD,
          [boolean(True), string("bar")]],
         Types.ComplexConditional),

        ([Types.ComplexConditional.KEYWORD,
          [boolean(False), string("bar")],
          [boolean(True), string("baz")]],
         Types.ComplexConditional),

        ([Types.Function.KEYWORD, integer(0)],         Types.Function),
        (['x', Types.Function.KEYWORD, integer(0)],    Types.Function),
        (['x', 'y', Types.Function.KEYWORD, 'x'],      Types.Function),
        (['x', 'y', 'z', Types.Function.KEYWORD, 'x'], Types.Function),

        ([Types.TailCallFunction.KEYWORD, integer(0)],         Types.TailCallFunction),
        (['x', Types.TailCallFunction.KEYWORD, integer(0)],    Types.TailCallFunction),
        (['x', 'y', Types.TailCallFunction.KEYWORD, 'x'],      Types.TailCallFunction),
        (['x', 'y', 'z', Types.TailCallFunction.KEYWORD, 'x'], Types.TailCallFunction),

        ([Types.List.KEYWORD, 'x', 'y', 'z'],              Types.List),
        ([Types.List.KEYWORD, integer(100), integer(200)], Types.List),

        ([Types.Object.KEYWORD], Types.Object),
    ]
    for contents, expected_type in data:
        form = Types.Form.infer_from(contents, Helpers.sample_environment())
        yield assert_equals, expected_type, type(form)

