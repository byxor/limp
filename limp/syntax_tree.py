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
        return (Types.String, token.contents)
    elif token.type_ == Tokens.Types.Hexadecimal:
        return numeric_tree(Types.Hexadecimal, token)
    elif token.type_ == Tokens.Types.Octal:
        return numeric_tree(Types.Octal, token)
    elif token.type_ == Tokens.Types.Binary:
        return numeric_tree(Types.Binary, token)
    elif token.type_ == Tokens.Types.OpenParenthesis:
        contents = [(Types.Symbol, tokens[1].contents)]

        i = 2
        while True:
            if tokens[i].type_ == Tokens.Types.CloseParenthesis:
                break
            else:
                contents.append(create_from(tokens[i:]))
            i += 1

        return (Types.FunctionCall, contents)
    else:
        return []


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


def numeric_tree(tree_type, token):
    sign = token.contents[0]
    if sign == "+":
        return (Types.UnaryPositive, (tree_type, token.contents[1:]))
    elif sign == "-":
        return (Types.UnaryNegative, (tree_type, token.contents[1:]))
    else:
        return (tree_type, token.contents)
