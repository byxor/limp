import limp.environment as Environment
import limp.tokens as Tokens
import limp.token_tree as TokenTree
import limp.types as Types
import test.helpers as Helpers
from nose.tools import assert_equals


def test_building_token_tree_from_source_code():
    data = [
        ('1',                  '1'),
        ('(+ 1 2)',            ['+','1','2']),
        ('(+ (- 1 2) 3)',      ['+',['-','1','2'],'3']),
        ('(run (time now) 5)', ['run',['time','now'],'5']),
    ]
    for source_code, expected_token_tree in data:
        token_tree = TokenTree.create_from(
            Tokens.create_from(source_code))
        yield assert_equals, expected_token_tree, token_tree


def test_evaluating_source_code():
    data = [
        ('1',             1),
        ('(+ 1 2)',       3),
        ('(+ (+ 1 2) 3)', 6),
        ('variable',      20),
        ('"Hello!"',      "Hello!"),
        ('(+\n1\t2)',     3),
    ]        
    for source_code, expected_result in data:
        result = Types.Form.infer_from(
            TokenTree.create_from(
                Tokens.create_from(source_code)),
            Helpers.SIMPLE_ENVIRONMENT
        ).evaluate()
        yield assert_equals, expected_result, result
