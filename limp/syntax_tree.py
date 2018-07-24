import limp.tokens as Tokens
from enum import Enum, auto, unique
from collections import namedtuple


@unique
class Types(Enum):
    Float = auto()
    Integer = auto()
    Binary = auto()
    Octal = auto()
    Hexadecimal = auto()
    String = auto()
    UnaryPositive = auto()
    UnaryNegative = auto()
    FunctionCall = auto()
    Symbol = auto()


def create_from(tokens):
    node = _search_for_node(tokens)
    if node:
        return node.tree


#############################################


def _search_for_node(chunk):
    for size in range(1, len(chunk) + 1):
        node = _get_node_for(chunk[:size])
        if node:
            return node


def _get_node_for(chunk):
    if len(chunk) == 1:
        return _node_from_single_token(chunk[0])
    elif len(chunk) >= 3:
        return _function_call_node(chunk)


def _node_from_single_token(token):
    if token.type_ == Tokens.Types.Integer:
        tree = numeric_tree(Types.Integer, token)
    elif token.type_ == Tokens.Types.Float:
        tree = numeric_tree(Types.Float, token)
    elif token.type_ == Tokens.Types.Hexadecimal:
        tree = numeric_tree(Types.Hexadecimal, token)
    elif token.type_ == Tokens.Types.Octal:
        tree = numeric_tree(Types.Octal, token)
    elif token.type_ == Tokens.Types.Binary:
        tree = numeric_tree(Types.Binary, token)
    elif token.type_ == Tokens.Types.String:
        tree = (Types.String, token.contents)
    else:
        return None
    return _Node(tree, 1)


def _function_call_node(chunk):
    opens =        chunk[0].type_  == Tokens.Types.OpenParenthesis
    has_function = chunk[1].type_  == Tokens.Types.Symbol
    closes =       chunk[-1].type_ == Tokens.Types.CloseParenthesis
    if opens and has_function and closes:
        arguments = [(Types.Symbol, chunk[1].contents)]
        
        i = 2
        while i < len(chunk) - 1:
            node = _search_for_node(chunk[i:])
            arguments.append(node.tree)
            i += node.tokens_consumed

        tokens_consumed = len(arguments) + 2
        return _Node((Types.FunctionCall, arguments), tokens_consumed)


_Node = namedtuple('_Node', 'tree tokens_consumed')


def numeric_tree(tree_type, token):
    sign = token.contents[0]
    if sign == "+":
        return (Types.UnaryPositive, (tree_type, token.contents[1:]))
    elif sign == "-":
        return (Types.UnaryNegative, (tree_type, token.contents[1:]))
    else:
        return (tree_type, token.contents)
