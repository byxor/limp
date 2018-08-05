import limp.tokens as Tokens
import limp.errors as Errors
from limp.parsing.shared import *


def node(tokens):
    opener = Tokens.Types.OpenCurlyBrace
    closer = Tokens.Types.CloseCurlyBrace

    if not opens_and_closes(tokens, opener, closer):
        return

    if not balanced(tokens, opener, closer):
        return

    trees, tokens_consumed = get_multiple_trees(tokens[1:-1])
    tokens_consumed += 2

    if len(trees) % 3 != 0:
        raise Errors.MalformedObject()

    pairs = []
    for i in range(0, len(trees), 3):
        key = trees[i]

        if trees[i+1][0] != Types.ObjectDelimiter:
            raise Errors.IncorrectObjectDelimiter()

        value = trees[i+2]
        pairs.append((key, value))


    return Node((Types.Object, pairs), tokens_consumed)
