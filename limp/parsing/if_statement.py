import limp.tokens as Tokens
import limp.syntax as Syntax
from limp.parsing.utils import *


def node(chunk):
    opener = Tokens.Types.OpenParenthesis
    closer = Tokens.Types.CloseParenthesis

    if not opens_and_closes(chunk, opener, closer):
        return

    if chunk[1] != (Tokens.Types.Symbol, Syntax.IF):
        return

    if not balanced(chunk, opener, closer):
        return

    contents, tokens_consumed = get_multiple_trees(chunk[2:-1])
    tokens_consumed += 3

    condition = contents[0]
    if_true = contents[1]
    if_false = None

    try:
        if_false = contents[2]
    except IndexError:
        if_false = None

    return Node((Types.IfStatement, condition, if_true, if_false),
                 tokens_consumed)
