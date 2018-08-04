import limp.tokens as Tokens
import limp.errors as Errors
from limp.parsing.shared import *


def node(tokens):
    opener = Tokens.Types.OpenParenthesis
    closer = Tokens.Types.CloseParenthesis

    if not opens_and_closes(tokens, opener, closer):
        return

    if not balanced(tokens, opener, closer):
        return

    trees, tokens_consumed = get_multiple_trees(tokens[1:-1])

    try:
        function = trees[0]
    except IndexError:
        raise Errors.EmptyFunctionCall()

    arguments = trees[1:]
    tokens_consumed += 2

    return Node((Types.FunctionCall, function, arguments), tokens_consumed)
