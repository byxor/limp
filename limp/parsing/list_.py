import limp.tokens as Tokens
from limp.parsing.shared import *


def node(tokens):
    opener = Tokens.Types.OpenSquareBracket
    closer = Tokens.Types.CloseSquareBracket

    if not opens_and_closes(tokens, opener, closer):
        return

    if not balanced(tokens, opener, closer):
        return

    contents, tokens_consumed = get_multiple_trees(tokens[1:-1])
    tokens_consumed += 2

    return Node((Types.List, contents), tokens_consumed)
