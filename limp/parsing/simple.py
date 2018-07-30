import limp.tokens as Tokens
from limp.parsing.utils import *


def float_node(tokens):
    if tokens[0].type_ == Tokens.Types.Float:
        return Node(_numeric_tree(Types.Float, tokens[0]), 1)


def integer_node(tokens):
    if tokens[0].type_ == Tokens.Types.Integer:
        return Node(_numeric_tree(Types.Integer, tokens[0]), 1)


def hexadecimal_node(tokens):
    if tokens[0].type_ == Tokens.Types.Hexadecimal:
        return Node(_numeric_tree(Types.Hexadecimal, tokens[0]), 1)


def octal_node(tokens):
    if tokens[0].type_ == Tokens.Types.Octal:
        return Node(_numeric_tree(Types.Octal, tokens[0]), 1)


def binary_node(tokens):
    if tokens[0].type_ == Tokens.Types.Binary:
        return Node(_numeric_tree(Types.Binary, tokens[0]), 1)


def _numeric_tree(tree_type, token):
    sign = token.contents[0]
    if sign == "+":
        return (Types.UnaryPositive, (tree_type, token.contents[1:]))
    elif sign == "-":
        return (Types.UnaryNegative, (tree_type, token.contents[1:]))
    else:
        return (tree_type, token.contents)


def string_node(tokens):
    if tokens[0].type_ == Tokens.Types.String:
        return Node((Types.String, tokens[0].contents), 1)


def boolean_node(tokens):
    if tokens[0].type_ == Tokens.Types.Boolean:
        return Node((Types.Boolean, tokens[0].contents), 1)


def symbol_node(tokens):
    if tokens[0].type_ == Tokens.Types.Symbol:
        return Node((Types.Symbol, tokens[0].contents), 1)


def object_delimiter_node(tokens):
    if tokens[0].type_ == Tokens.Types.ObjectDelimiter:
        return Node((Types.Symbol, tokens[0].contents), 1)
