import limp.tokens as Tokens
import limp.syntax as Syntax
from limp.parsing.shared import *


def node(tokens):
    opener = Tokens.Types.OpenParenthesis
    closer = Tokens.Types.CloseParenthesis

    if not opens_and_closes(tokens, opener, closer):
        return

    if tokens[1] != (Tokens.Types.Symbol, Syntax.IF):
        return

    if not balanced(tokens, opener, closer):
        return

    contents, tokens_consumed = get_multiple_trees(tokens[2:-1])
    tokens_consumed += 3

    condition = contents[0]
    if_true = contents[1]
    if_false = None

    try:
        if_false = contents[2]
    except IndexError:
        if_false = None

    tree = (Types.IfStatement, condition, if_true, if_false)
    return Node(tree, tokens_consumed)
