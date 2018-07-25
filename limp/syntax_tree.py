import limp.tokens as Tokens
from enum import Enum, auto, unique
from collections import namedtuple


@unique
class Types(Enum):
    Float         = auto()
    Boolean       = auto()
    Integer       = auto()
    Binary        = auto()
    Octal         = auto()
    Hexadecimal   = auto()
    String        = auto()
    UnaryPositive = auto()
    UnaryNegative = auto()
    Function      = auto()
    FunctionCall  = auto()
    Symbol        = auto()
    List          = auto()


def create_from(tokens):
    node = _search_for_node(tokens)
    if node:
        return node.tree


def _search_for_node(chunk):
    for size in range(1, len(chunk) + 1):
        node = _get_node_for(chunk[:size])
        if node:
            return node


def _get_node_for(chunk):
    if len(chunk) == 1:
        return _node_from_single_token(chunk[0])

    if len(chunk) >= 2:
        node = _list_node(chunk)
        if node:
            return node

    if len(chunk) >= 4:
        node = _function_node(chunk)
        if node:
            return node

    if len(chunk) >= 3:
        node = _function_call_node(chunk)
        if node:
            return node


def _node_from_single_token(token):
    if token.type_ == Tokens.Types.Float:
        tree = _numeric_tree(Types.Float, token)
    elif token.type_ == Tokens.Types.Integer:
        tree = _numeric_tree(Types.Integer, token)
    elif token.type_ == Tokens.Types.Hexadecimal:
        tree = _numeric_tree(Types.Hexadecimal, token)
    elif token.type_ == Tokens.Types.Octal:
        tree = _numeric_tree(Types.Octal, token)
    elif token.type_ == Tokens.Types.Binary:
        tree = _numeric_tree(Types.Binary, token)
    elif token.type_ == Tokens.Types.String:
        tree = (Types.String, token.contents)
    elif token.type_ == Tokens.Types.Boolean:
        tree = (Types.Boolean, token.contents)
    elif token.type_ == Tokens.Types.Symbol:
        tree = (Types.Symbol, token.contents)
    else:
        return None
    return _Node(tree, 1)


def _numeric_tree(tree_type, token):
    sign = token.contents[0]
    if sign == "+":
        return (Types.UnaryPositive, (tree_type, token.contents[1:]))
    elif sign == "-":
        return (Types.UnaryNegative, (tree_type, token.contents[1:]))
    else:
        return (tree_type, token.contents)


def _list_node(chunk):
    if chunk[0].type_ != Tokens.Types.OpenSquareBracket:
        return

    if chunk[-1].type_ != Tokens.Types.CloseSquareBracket:
        return
    
    openings = len([t for t in chunk if t.type_ == Tokens.Types.OpenSquareBracket])
    closings = len([t for t in chunk if t.type_ == Tokens.Types.CloseSquareBracket])
    if openings != closings:
        return
    
    contents, tokens_consumed = _get_multiple_trees(chunk[1:])
    tokens_consumed += 2

    return _Node((Types.List, contents), tokens_consumed)


def _function_call_node(chunk):
    if chunk[0].type_ != Tokens.Types.OpenParenthesis:
        return

    if chunk[-1].type_ != Tokens.Types.CloseParenthesis:
        return

    openings = len([t for t in chunk if t.type_ == Tokens.Types.OpenParenthesis])
    closings = len([t for t in chunk if t.type_ == Tokens.Types.CloseParenthesis])
    if openings != closings:
        return

    trees, tokens_consumed = _get_multiple_trees(chunk[1:-1])

    function = trees[0]
    arguments = trees[1:]
    tokens_consumed += 2

    return _Node((Types.FunctionCall, function, arguments), tokens_consumed)
    

def _function_node(chunk):
    if chunk[0].type_ != Tokens.Types.OpenParenthesis:
        return

    if chunk[-1].type_ != Tokens.Types.CloseParenthesis:
        return

    openings = len([t for t in chunk if t.type_ == Tokens.Types.OpenParenthesis])
    closings = len([t for t in chunk if t.type_ == Tokens.Types.CloseParenthesis])
    if openings != closings:
        return

    delimiter = _get_function_delimiter_position(chunk)
    if not delimiter:
        return

    argument_chunk = chunk[1:delimiter]
    for token in argument_chunk:
        if token.type_ != Tokens.Types.Symbol:
            return

    argument_trees, _ = _get_multiple_trees(argument_chunk)

    body_chunk = chunk[delimiter+1:-1]
    body_node = _get_node_for(body_chunk)

    return _Node((Types.Function, argument_trees, body_node.tree), 4)


def _get_function_delimiter_position(chunk):
    for i in range(1, len(chunk) - 1):
        if chunk[i].type_ == Tokens.Types.FunctionDelimiter:
            return i


def _get_multiple_trees(chunk):
    trees = []
    tokens_consumed = 0
    
    start = 0
    while start < len(chunk):
        node = _search_for_node(chunk[start:])
        if node:
            trees.append(node.tree)
            start += node.tokens_consumed
            tokens_consumed += node.tokens_consumed
        else:
            start += 1

    return trees, tokens_consumed


_Node = namedtuple('_Node', 'tree tokens_consumed')
