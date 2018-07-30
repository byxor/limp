import limp.tokens as Tokens
from limp.parsing.shared import *


def node(tokens):
    opener = Tokens.Types.OpenParenthesis
    closer = Tokens.Types.CloseParenthesis

    if not opens_and_closes(tokens, opener, closer):
        return

    if not balanced(tokens, opener, closer):
        return

    delimiter = _delimiter_position(tokens)
    if not delimiter:
        return

    argument_tokens = tokens[1:delimiter]
    if not _all_symbols(argument_tokens):
        return

    argument_trees, tokens_consumed = get_multiple_trees(argument_tokens)

    import limp.syntax_tree as SyntaxTree
    body_tokens = tokens[delimiter + 1:-1]
    body_node = SyntaxTree.get_node_for(body_tokens)

    tokens_consumed += body_node.tokens_consumed
    tokens_consumed += 3

    return Node((Types.Function, argument_trees, body_node.tree), tokens_consumed)


def _all_symbols(tokens):
    for token in tokens:
        if token.type_ != Tokens.Types.Symbol:
            return False
    return True


def _delimiter_position(tokens):
    for i, token in enumerate(tokens):
        if token.type_ == Tokens.Types.FunctionDelimiter:
            return i


