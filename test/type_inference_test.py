import limp.types as Types
import test.helpers as Helpers
from nose.tools import assert_equals


def test_type_inference():
    data = [
        ('abc',      Types.Symbol),
        ('def',      Types.Symbol),
        ('123',      Types.Integer),
        ('456',      Types.Integer),
        ('1.2',      Types.Float),
        ('2.4',      Types.Float),
        ('0x5',      Types.Hexadecimal),
        ('0xABC',    Types.Hexadecimal),
        ('0b1',      Types.Binary),
        ('0b101011', Types.Binary),

        ('true',          Types.Boolean),
        ('false',         Types.Boolean),
        ('"Github!"',     Types.String),
        ('"Hello there"', Types.String),
        
        (['define', 'x', '10'], Types.Definition),
        (['define', 'y', '20'], Types.Definition),
        (['+', '0', '1'],       Types.Invocation),
        (['return10'],          Types.Invocation),
        (['do'],                Types.SequentialEvaluator),
        (['do', 'x', 'y', 'z'], Types.SequentialEvaluator),
        (['if', 'true', 'x'],   Types.SimpleConditional),
        (['if', 'false', 'y'],  Types.SimpleConditional),
        
        (['condition', ['true', '"bar"']],                     Types.ComplexConditional),
        (['condition', ['false', '"bar"'], ['true', '"baz"']], Types.ComplexConditional),
        
        (['function', [], '0'],                     Types.Function),
        (['function', ['x', 'y'], ['+', 'x', 'y']], Types.Function),

        (['list', 'x', 'y', 'z'], Types.List),
        (['list', '100', '200'],  Types.List),
    ]
    for contents, expected_type in data:
        form = Types.Form.infer_from(contents, Helpers.sample_environment())
        yield assert_equals, expected_type, type(form)
