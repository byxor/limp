import limp.tokens as Tokens
from limp.parsing.utils import *


def node(chunk):
    opener = Tokens.Types.OpenSquareBracket
    closer = Tokens.Types.CloseSquareBracket

    if not opens_and_closes(chunk, opener, closer):
        return

    if not balanced(chunk, opener, closer):
        return

    contents, tokens_consumed = get_multiple_trees(chunk[1:-1])
    tokens_consumed += 2

    return Node((Types.List, contents), tokens_consumed)
