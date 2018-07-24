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
    print(f'SEARCH THRU: {" ".join([str(t.contents) for t in chunk])}')
    for size in range(1, len(chunk) + 1):

        print(f'Get node for: {" ".join([str(t.contents) for t in chunk[:size]])}')

        node = _get_node_for(chunk[:size])
        if node:

            print(f"   got one: {node}")

            return node
        else:
            print(f"   nuthin")


def _get_node_for(chunk):
    if len(chunk) == 1:
        return _node_from_single_token(chunk[0])
    elif len(chunk) >= 3:
        return _function_call_node(chunk)


def _node_from_single_token(token):
    if token.type_ == Tokens.Types.Integer:
        tree = _numeric_tree(Types.Integer, token)
    elif token.type_ == Tokens.Types.Float:
        tree = _numeric_tree(Types.Float, token)
    elif token.type_ == Tokens.Types.Hexadecimal:
        tree = _numeric_tree(Types.Hexadecimal, token)
    elif token.type_ == Tokens.Types.Octal:
        tree = _numeric_tree(Types.Octal, token)
    elif token.type_ == Tokens.Types.Binary:
        tree = _numeric_tree(Types.Binary, token)
    elif token.type_ == Tokens.Types.String:
        tree = (Types.String, token.contents)
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


def _function_call_node(chunk):
    openings = len([t for t in chunk if t.type_ == Tokens.Types.OpenParenthesis])
    closings = len([t for t in chunk if t.type_ == Tokens.Types.CloseParenthesis])

    has_function = chunk[1].type_ == Tokens.Types.Symbol

    if (openings == closings) and has_function:
        function = (Types.Symbol, chunk[1].contents)

        arguments = []        
        i = 2
        while i < len(chunk) - 1:

            depth = 0
            j = i
            while j < len(chunk):
                if chunk[j].type_ == Tokens.Types.OpenParenthesis:
                    depth += 1
                elif chunk[j].type_ == Tokens.Types.CloseParenthesis:
                    depth -= 1
                if depth == 0:
                    break
                j += 1

            print(i, j)

            node = _search_for_node(chunk[i:j+1])
            arguments.append(node.tree)
            i += node.tokens_consumed

        tokens_consumed = (i - 2) + 3
        return _Node((Types.FunctionCall, function, arguments), tokens_consumed)


_Node = namedtuple('_Node', 'tree tokens_consumed')
