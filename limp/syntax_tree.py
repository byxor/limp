import limp.tokens as Tokens
from enum import Enum, auto, unique


def create_from(tokens):
    if len(tokens) == 0:
        return []
    
    token = tokens[0]
    if token.type_ == Tokens.Types.Integer:
        return integer_tree(token)
    elif token.type_ == Tokens.Types.Float:
        return float_tree(token)
    elif token.type_ == Tokens.Types.String:
        return [(Types.String, token.contents)]


@unique
class Types(Enum):
    Integer = auto()
    Float = auto()
    String = auto()
    UnaryPositive = auto()
    UnaryNegative = auto()


def integer_tree(token):
    return number_tree(Types.Integer, token)


def float_tree(token):
    return number_tree(Types.Float, token)


def number_tree(tree_type, token):
    sign = token.contents[0]
    if sign == "+":
        return [(Types.UnaryPositive, (tree_type, token.contents[1:]))]
    elif sign == "-":
        return [(Types.UnaryNegative, (tree_type, token.contents[1:]))]
    else:
        return [(tree_type, token.contents)]
