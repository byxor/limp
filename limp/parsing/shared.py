import limp.tokens as Tokens
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
    Conditional = auto()


Node = namedtuple('_Node', 'tree tokens_consumed')


def get_multiple_trees(tokens):
    trees = []
    tokens_consumed = 0

    start = 0
    while start < len(tokens):
        node = search_for_node(tokens[start:])
        if node:
            trees.append(node.tree)
            start += node.tokens_consumed
            tokens_consumed += node.tokens_consumed
        else:
            start += 1

    return trees, tokens_consumed


def opens_and_closes(tokens, opener, closer):
    opens = tokens[0].type_ == opener
    closes = tokens[-1].type_ == closer
    return opens and closes


def balanced(tokens, opener, closer):
    count = lambda token_type: len([t for t in tokens if t.type_ == token_type])
    return count(opener) == count(closer)


def search_for_node(tokens):
    return _perform_search(tokens, lookahead)


def search_for_node_no_lookahead(tokens):
    return _perform_search(tokens, None)


def _perform_search(tokens, lookahead):
    import limp.syntax_tree as SyntaxTree
    for size in range(1, len(tokens) + 1):
        node = SyntaxTree.get_node_for(tokens[:size])
        if node:
            if lookahead:
                new_node = lookahead(node, tokens[size:])
                if new_node:
                    return new_node
            return node


def lookahead(node, tokens):
    attribute_access_nodes = [node]

    i = 0
    while i < len(tokens):
        if tokens[i].type_ == Tokens.Types.AttributeAccessDelimiter:
            future_tokens = tokens[i+1:]
            future_node = search_for_node_no_lookahead(future_tokens)
            attribute_access_nodes.append(future_node)
            i += future_node.tokens_consumed + 1
        else:
            break

    tokens_consumed = sum([n.tokens_consumed for n in attribute_access_nodes])
    tokens_consumed += len(attribute_access_nodes) - 1

    if len(attribute_access_nodes) > 1:
        return Node(_transform(attribute_access_nodes), tokens_consumed)


def _transform(nodes):
    if len(nodes) == 2:
        return (Types.AttributeAccess, nodes[0].tree, nodes[1].tree)
    return (Types.AttributeAccess, _transform(nodes[:-1]), nodes[-1].tree)
