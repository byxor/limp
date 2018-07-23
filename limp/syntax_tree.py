import limp.tokens as Tokens
from enum import Enum, auto, unique


def create_from(tokens):
    if len(tokens) == 0:
        return []
    
    token = tokens[0]
    if token.type_ == Tokens.Types.Integer:
        return numeric_tree(Types.Integer, token)
    elif token.type_ == Tokens.Types.Float:
        return numeric_tree(Types.Float, token)
    elif token.type_ == Tokens.Types.String:
        return [(Types.String, token.contents)]
    elif token.type_ == Tokens.Types.Hexadecimal:
        return numeric_tree(Types.Hexadecimal, token)
    else:
        return numeric_tree(Types.Octal, token)


@unique
class Types(Enum):
    Integer = auto()
    Float = auto()
    Octal = auto()
    Hexadecimal = auto()
    String = auto()
    UnaryPositive = auto()
    UnaryNegative = auto()


def numeric_tree(tree_type, token):
    sign = token.contents[0]
    if sign == "+":
        return [(Types.UnaryPositive, (tree_type, token.contents[1:]))]
    elif sign == "-":
        return [(Types.UnaryNegative, (tree_type, token.contents[1:]))]
    else:
        return [(tree_type, token.contents)]
