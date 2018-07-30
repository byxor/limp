import limp.tokens as Tokens
from enum import Enum, auto, unique
from limp.parsing.node import Node


def get_multiple_trees(chunk):
    trees = []
    tokens_consumed = 0
    start = 0
    while start < len(chunk):
        node = search_for_node(chunk[start:])
        if node:
            trees.append(node.tree)
            start += node.tokens_consumed
            tokens_consumed += node.tokens_consumed
    return trees, tokens_consumed


def opens_and_closes(chunk, opener, closer):
    opens = chunk[0].type_ == opener
    closes = chunk[-1].type_ == closer
    return opens and closes


def balanced(chunk, opener, closer):
    count = lambda token_type: len([t for t in chunk if t.type_ == token_type])
    return count(opener) == count(closer)


def search_for_node(chunk):
    return foo(chunk, lookahead)


def search_for_node_no_lookahead(chunk):
    return foo(chunk, None)


def foo(chunk, lookahead):
    import limp.syntax_tree as SyntaxTree
    for size in range(1, len(chunk) + 1):
        node = SyntaxTree.get_node_for(chunk[:size])
        if node:
            if lookahead:
                new_node = lookahead(node, chunk[size:])
                if new_node:
                    return new_node
            return node
    

def lookahead(node, chunk):
    attribute_access_nodes = [node]

    i = 0
    while i < len(chunk):
        if chunk[i].type_ == Tokens.Types.AttributeAccessDelimiter:
            future_chunk = chunk[i+1:]
            future_node = search_for_node_no_lookahead(future_chunk)
            attribute_access_nodes.append(future_node)
            i += future_node.tokens_consumed + 1
        else:
            break
            
    tokens_consumed = sum([n.tokens_consumed for n in attribute_access_nodes])
    tokens_consumed += len(attribute_access_nodes) - 1
            
    if len(attribute_access_nodes) > 1:
        return Node(transform(attribute_access_nodes), tokens_consumed)


def transform(nodes):
    if len(nodes) == 2:
        return (Types.AttributeAccess, nodes[0].tree, nodes[1].tree)
    return (Types.AttributeAccess, transform(nodes[:-1]), nodes[-1].tree)


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
