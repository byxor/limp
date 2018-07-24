import limp.tokens as Tokens
from enum import Enum, auto, unique
from collections import namedtuple


@unique
class Types(Enum):
    Float         = auto()
    Integer       = auto()
    Binary        = auto()
    Octal         = auto()
    Hexadecimal   = auto()
    String        = auto()
    UnaryPositive = auto()
    UnaryNegative = auto()
    FunctionCall  = auto()
    Symbol        = auto()
    List          = auto()


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

    if len(chunk) >= 2:
        node = _list_node(chunk)
        if node:
            return node

    if len(chunk) >= 3:
        node = _function_call_node(chunk)
        if node:
            return node


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


def _list_node(chunk):
    if chunk[-1].type_ != Tokens.Types.CloseSquareBracket:
        return
    
    openings = len([t for t in chunk if t.type_ == Tokens.Types.OpenSquareBracket])
    closings = len([t for t in chunk if t.type_ == Tokens.Types.CloseSquareBracket])

    if openings == closings:
        contents = []
    
        tokens_consumed = 2

        start = 1
        while start < len(chunk) - 1:
            end = _get_end_of_list(chunk, start)
            print(start, end)
            node = _search_for_node(chunk[start:end])
            contents.append(node.tree)
            start += node.tokens_consumed
            tokens_consumed += node.tokens_consumed

        return _Node((Types.List, contents), tokens_consumed)


def _function_call_node(chunk):
    openings = len([t for t in chunk if t.type_ == Tokens.Types.OpenParenthesis])
    closings = len([t for t in chunk if t.type_ == Tokens.Types.CloseParenthesis])

    has_function = chunk[1].type_ == Tokens.Types.Symbol

    if (openings == closings) and has_function:
        function = (Types.Symbol, chunk[1].contents)

        arguments = []        
        start = 2
        while start < len(chunk) - 1:
            end = _get_end_of_function_call(chunk, start)
            node = _search_for_node(chunk[start:end])
            arguments.append(node.tree)
            start += node.tokens_consumed

        tokens_consumed = (start - 2) + 3
        return _Node((Types.FunctionCall, function, arguments), tokens_consumed)


def _get_end_of_function_call(chunk, start):
    depth = 0
    end = start
    while end < len(chunk):
        if chunk[end].type_ == Tokens.Types.OpenParenthesis:
            depth += 1
        elif chunk[end].type_ == Tokens.Types.CloseParenthesis:
            depth -= 1
        if depth == 0:
            break
        end += 1
    return end + 1


def _get_end_of_list(chunk, start):
    end = start
    while end < len(chunk):
        if chunk[end].type_ == Tokens.Types.CloseSquareBracket:
            return end + 1
        end += 1


_Node = namedtuple('_Node', 'tree tokens_consumed')
