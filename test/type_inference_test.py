import limp.types as Types
import test.helpers as Helpers
from nose.tools import assert_equals


def test_type_inference():
    data = [
        ('abc',                 Types.Symbol),
        ('def',                 Types.Symbol),
        ('123',                 Types.Integer),
        ('456',                 Types.Integer),
        ('1.2',                 Types.Float),
        ('2.4',                 Types.Float),
        ('0x5',                 Types.Hexadecimal),
        ('0xABC',               Types.Hexadecimal),
        ('0b1',                 Types.Binary),
        ('0b101011',            Types.Binary),
        (['define', 'x', '10'], Types.Definition),
        (['define', 'y', '20'], Types.Definition),
        (['+', '0', '1'],       Types.Invocation),
        (['return10'],          Types.Invocation),
        ('true',                Types.Boolean),
        ('false',               Types.Boolean),
        ('"Github!"',           Types.String),
        ('"Hello there"',       Types.String),
        (['do'],                Types.SequentialEvaluator),
    ]
    for contents, expected_type in data:
        form = Types.Form.infer_from(contents, Helpers.SIMPLE_ENVIRONMENT)
        yield assert_equals, expected_type, type(form)
