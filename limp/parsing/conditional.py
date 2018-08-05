import limp.tokens as Tokens
import limp.syntax as Syntax
from limp.parsing.shared import *


def node(tokens):
    if tokens[0].contents != Syntax.CONDITIONAL:
        return

    if len(tokens) < 5:
        return

    condition_tokens = tokens[1:]

    opener = Tokens.Types.OpenCurlyBrace
    closer = Tokens.Types.CloseCurlyBrace

    if not opens_and_closes(condition_tokens, opener, closer):
        return

    if not balanced(condition_tokens, opener, closer):
        return

    trees, tokens_consumed = get_multiple_trees(condition_tokens[1:-1])
    tokens_consumed += 3

    pairs = []
    default_return_value = None
    for i in range(0, len(trees), 3):
        if i + 1 >= len(trees):
            default_return_value = trees[i]
        else:
            condition = trees[i]
            value = trees[i+2]
            pairs.append((condition, value))

    return Node((Types.Conditional, pairs, default_return_value), tokens_consumed)
