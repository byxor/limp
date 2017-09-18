from nose.tools import assert_equals
import limp.token_tree as TokenTree


def test_complex_input():
    data = [
        (['1'],                                 '1'),
        (['(','do_stuff',')'],                  ['do_stuff']),
        (['(','+','1','2',')'],                 ['+','1','2']),
        (['(','send','10',')'],                 ['send', '10']),
        (['(','+','1','(','-','2','3',')',')'], ['+','1',['-','2','3']]),
        (['(','%','(','+','1','2',')','3',')'], ['%',['+','1','2'],'3']),
    ]
    for tokens, expected_token_tree in data:
        yield assert_equals, expected_token_tree, TokenTree.create_from(tokens)
