import limp.tokens as Tokens
import limp.syntax as Syntax
import functools
from limp.parsing.shared import *


def _apply_sign(node):
    tree = node[0]
    contents = tree[1]

    sign = contents[0]

    if sign == Syntax.POSITIVE:
        type_ = Types.UnaryPositive
    elif sign == Syntax.NEGATIVE:
        type_ = Types.UnaryNegative
    else:
        return node

    return Node((type_, (tree[0], contents[1:])), 1)


def _node(mutator, tree_type, token_type):
    def internal(tokens):
        if tokens[0].type_ == token_type:
            tree = (tree_type, tokens[0].contents)
            node = Node(tree, 1)
            return mutator(node)
    return internal


_basic_node = functools.partial(_node, lambda n: n)
_numeric_node = functools.partial(_node, _apply_sign)


float_node       = _numeric_node(Types.Float, Tokens.Types.Float)
octal_node       = _numeric_node(Types.Octal, Tokens.Types.Octal)
binary_node      = _numeric_node(Types.Binary, Tokens.Types.Binary)
integer_node     = _numeric_node(Types.Integer, Tokens.Types.Integer)
hexadecimal_node = _numeric_node(Types.Hexadecimal, Tokens.Types.Hexadecimal)

string_node           = _basic_node(Types.String, Tokens.Types.String)
boolean_node          = _basic_node(Types.Boolean, Tokens.Types.Boolean)
object_delimiter_node = _basic_node(Types.ObjectDelimiter, Tokens.Types.ObjectDelimiter)


def symbol_node(tokens):
    if tokens[0].contents == Syntax.CONDITIONAL:
        return
    return _basic_node(Types.Symbol, Tokens.Types.Symbol)(tokens)
