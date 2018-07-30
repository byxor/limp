import limp.tokens as Tokens
from limp.parsing.utils import *


def node(chunk):
    opener = Tokens.Types.OpenParenthesis
    closer = Tokens.Types.CloseParenthesis

    if not opens_and_closes(chunk, opener, closer):
        return

    if not balanced(chunk, opener, closer):
        return

    delimiter = _get_delimiter_position(chunk)
    if not delimiter:
        return

    tokens_consumed = 3

    argument_chunk = chunk[1:delimiter]
    for token in argument_chunk:
        if token.type_ != Tokens.Types.Symbol:
            return
        tokens_consumed += 1

    argument_trees, _ = get_multiple_trees(argument_chunk)

    import limp.syntax_tree as SyntaxTree
    body_chunk = chunk[delimiter + 1:-1]
    body_node = SyntaxTree.get_node_for(body_chunk)
    tokens_consumed += body_node.tokens_consumed

    return Node((Types.Function, argument_trees, body_node.tree), tokens_consumed)


def _get_delimiter_position(chunk):
    for i, token in enumerate(chunk):
        if token.type_ == Tokens.Types.FunctionDelimiter:
            return i


