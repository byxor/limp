import limp.tokens as Tokens
from limp.parsing.shared import *


def node(chunk):
    opener = Tokens.Types.OpenCurlyBrace
    closer = Tokens.Types.CloseCurlyBrace

    if not opens_and_closes(chunk, opener, closer):
        return

    if not balanced(chunk, opener, closer):
        return

    trees, tokens_consumed = get_multiple_trees(chunk[1:-1])
    tokens_consumed += 2

    pairs = []
    for i in range(0, len(trees), 3):
        key = trees[i]
        value = trees[i+2]
        pairs.append((key, value))

    return Node((Types.Object, pairs), tokens_consumed)
