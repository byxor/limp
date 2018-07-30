import limp.tokens as Tokens
from limp.parsing.utils import *


def node(chunk):
    opener = Tokens.Types.OpenParenthesis
    closer = Tokens.Types.CloseParenthesis

    if not opens_and_closes(chunk, opener, closer):
        return

    if not balanced(chunk, opener, closer):
        return

    trees, tokens_consumed = get_multiple_trees(chunk[1:-1])

    function = trees[0]
    arguments = trees[1:]
    tokens_consumed += 2

    return Node((Types.FunctionCall, function, arguments), tokens_consumed)

