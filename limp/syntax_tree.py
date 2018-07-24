import limp.tokens as Tokens
from enum import Enum, auto, unique
from collections import namedtuple, Iterable


def create_from(tokens):
    if len(tokens) == 0:
        return []
    return _search_for_node(tokens)[0]


def _search_for_node(chunk):
    end = 1
    while end <= len(chunk):
        try:
            return _get_node(chunk[:end])
        except NodeNotFound:
            end += 1
    raise NodeNotFound(chunk)


def _get_node(chunk):
    if len(chunk) == 1:
        if chunk[0].type_ == Tokens.Types.Integer:
            return (numeric_tree(Types.Integer, chunk[0]), 1)
        elif chunk[0].type_ == Tokens.Types.Float:
            return (numeric_tree(Types.Float, chunk[0]), 1)
        elif chunk[0].type_ == Tokens.Types.Hexadecimal:
            return (numeric_tree(Types.Hexadecimal, chunk[0]), 1)
        elif chunk[0].type_ == Tokens.Types.Octal:
            return (numeric_tree(Types.Octal, chunk[0]), 1)
        elif chunk[0].type_ == Tokens.Types.Binary:
            return (numeric_tree(Types.Binary, chunk[0]), 1)
        elif chunk[0].type_ == Tokens.Types.String:
            return ((Types.String, chunk[0].contents), 1)
    elif len(chunk) >= 3:
        opens = chunk[0].type_ == Tokens.Types.OpenParenthesis
        has_function = chunk[1].type_ == Tokens.Types.Symbol
        closes = chunk[-1].type_ == Tokens.Types.CloseParenthesis
        if opens and has_function and closes:
            arguments = [(Types.Symbol, chunk[1].contents)]

            i = 2
            while i < len(chunk) - 1:
                node, tokens_consumed = _search_for_node(chunk[i:])
                arguments.append(node)
                i += tokens_consumed

            return ((Types.FunctionCall, arguments), len(arguments) + 2)

    raise NodeNotFound(chunk)


class NodeNotFound(Exception):
    def __init__(self, chunk):
        super().__init__(f"Node not found in {chunk}")


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
    Nothing = auto()


def numeric_tree(tree_type, token):
    sign = token.contents[0]
    if sign == "+":
        return (Types.UnaryPositive, (tree_type, token.contents[1:]))
    elif sign == "-":
        return (Types.UnaryNegative, (tree_type, token.contents[1:]))
    else:
        return (tree_type, token.contents)
