import limp.tokens as Tokens
import limp.syntax as Syntax
from enum import Enum, auto, unique
from collections import namedtuple


@unique
class Types(Enum):
    Float = auto()
    Boolean = auto()
    Integer = auto()
    Binary = auto()
    Octal = auto()
    Hexadecimal = auto()
    String = auto()
    UnaryPositive = auto()
    UnaryNegative = auto()
    Function = auto()
    FunctionCall = auto()
    IfStatement = auto()
    Symbol = auto()
    List = auto()
    Object = auto()
    ObjectDelimiter = auto()
    AttributeAccess = auto()


def create_from(tokens):
    node = _search_for_node(tokens)
    if node:
        return node.tree


def _search_for_node(chunk):
    for size in range(1, len(chunk) + 1):
        node = _get_node_for(chunk[:size])
        if node:
            
            ##########################################################
            # Special shit: look ahead to check for attribute access #
            ##########################################################
            # Please refactor this into its own function #
            ##############################################
            # Please... #
            #############

            attribute_access_nodes = [node]

            i = size
            while i < len(chunk):
                if chunk[i].type_ == Tokens.Types.AttributeAccessDelimiter:
                    future_chunk = chunk[i+1:]
                    future_node = _search_for_node_no_lookahead(future_chunk)
                    attribute_access_nodes.append(future_node)
                    i += future_node.tokens_consumed + 1
                else:
                    break
            
            tokens_consumed = sum([n.tokens_consumed for n in attribute_access_nodes])
            tokens_consumed += len(attribute_access_nodes) - 1
            
            if len(attribute_access_nodes) > 1:
                return _Node(_transform(attribute_access_nodes), tokens_consumed)

            ##############################################################

            return node


def _search_for_node_no_lookahead(chunk):
    for size in range(1, len(chunk) + 1):
        node = _get_node_for(chunk[:size])
        if node:
            return node


def _transform(nodes):
    if len(nodes) == 2:
        return (Types.AttributeAccess, nodes[0].tree, nodes[1].tree)
    return (Types.AttributeAccess, _transform(nodes[:-1]), nodes[-1].tree)


def _get_node_for(chunk):
    if len(chunk) == 1:
        return _node_from_single_token(chunk[0])

    if len(chunk) >= 2:
        node = _list_node(chunk)
        if node:
            return node

        node = _object_node(chunk)
        if node:
            return node

    if len(chunk) >= 5:
        node = _if_statement_node(chunk)
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
    elif token.type_ == Tokens.Types.ObjectDelimiter:
        tree = (Types.ObjectDelimiter, token.contents)
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


def _if_statement_node(chunk):
    opener = Tokens.Types.OpenParenthesis
    closer = Tokens.Types.CloseParenthesis

    if not _opens_and_closes(chunk, opener, closer):
        return

    if chunk[1] != (Tokens.Types.Symbol, Syntax.IF):
        return

    if not _balanced(chunk, opener, closer):
        return

    contents, tokens_consumed = _get_multiple_trees(chunk[2:-1])
    tokens_consumed += 3

    condition = contents[0]
    if_true = contents[1]
    if_false = None

    try:
        if_false = contents[2]
    except IndexError:
        if_false = None

    return _Node((Types.IfStatement, condition, if_true, if_false),
                 tokens_consumed)


def _object_node(chunk):
    opener = Tokens.Types.OpenCurlyBrace
    closer = Tokens.Types.CloseCurlyBrace

    if not _opens_and_closes(chunk, opener, closer):
        return

    if not _balanced(chunk, opener, closer):
        return

    trees, tokens_consumed = _get_multiple_trees(chunk[1:-1])
    tokens_consumed += 2

    pairs = []
    for i in range(0, len(trees), 3):
        key = trees[i]
        value = trees[i+2]
        pairs.append((key, value))

    return _Node((Types.Object, pairs), tokens_consumed)


def _list_node(chunk):
    opener = Tokens.Types.OpenSquareBracket
    closer = Tokens.Types.CloseSquareBracket

    if not _opens_and_closes(chunk, opener, closer):
        return

    if not _balanced(chunk, opener, closer):
        return

    contents, tokens_consumed = _get_multiple_trees(chunk[1:-1])
    tokens_consumed += 2

    return _Node((Types.List, contents), tokens_consumed)


def _function_call_node(chunk):
    opener = Tokens.Types.OpenParenthesis
    closer = Tokens.Types.CloseParenthesis

    if not _opens_and_closes(chunk, opener, closer):
        return

    if not _balanced(chunk, opener, closer):
        return

    trees, tokens_consumed = _get_multiple_trees(chunk[1:-1])

    function = trees[0]
    arguments = trees[1:]
    tokens_consumed += 2

    return _Node((Types.FunctionCall, function, arguments), tokens_consumed)


def _function_node(chunk):
    opener = Tokens.Types.OpenParenthesis
    closer = Tokens.Types.CloseParenthesis

    if not _opens_and_closes(chunk, opener, closer):
        return

    if not _balanced(chunk, opener, closer):
        return

    delimiter = _get_function_delimiter_position(chunk)
    if not delimiter:
        return

    tokens_consumed = 3

    argument_chunk = chunk[1:delimiter]
    for token in argument_chunk:
        if token.type_ != Tokens.Types.Symbol:
            return
        tokens_consumed += 1

    argument_trees, _ = _get_multiple_trees(argument_chunk)

    body_chunk = chunk[delimiter + 1:-1]
    body_node = _get_node_for(body_chunk)
    tokens_consumed += body_node.tokens_consumed

    return _Node((Types.Function, argument_trees, body_node.tree),
                 tokens_consumed)


def _get_function_delimiter_position(chunk):
    for i, token in enumerate(chunk):
        if token.type_ == Tokens.Types.FunctionDelimiter:
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
    return trees, tokens_consumed


def _opens_and_closes(chunk, opener, closer):
    opens = chunk[0].type_ == opener
    closes = chunk[-1].type_ == closer
    return opens and closes


def _balanced(chunk, opener, closer):
    count = lambda token_type: len([t for t in chunk if t.type_ == token_type])
    return count(opener) == count(closer)


_Node = namedtuple('_Node', 'tree tokens_consumed')
