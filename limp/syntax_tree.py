import limp.parsing.list_
import limp.parsing.simple
import limp.parsing.object_
import limp.parsing.function
import limp.parsing.function_call
import limp.parsing.conditional
from limp.parsing.shared import *
from enum import Enum, auto, unique


def create_from(tokens):
    node = search_for_node(tokens)
    if node:
        return node.tree


def get_node_for(chunk):
    for function in _NODE_FUNCTIONS:
        node = function(chunk)
        if node:
            return node


_NODE_FUNCTIONS = [
    limp.parsing.simple.float_node,
    limp.parsing.simple.integer_node,
    limp.parsing.simple.hexadecimal_node,
    limp.parsing.simple.octal_node,
    limp.parsing.simple.binary_node,
    limp.parsing.simple.string_node,
    limp.parsing.simple.boolean_node,
    limp.parsing.simple.object_delimiter_node,
    limp.parsing.conditional.node,
    limp.parsing.simple.symbol_node,
    limp.parsing.list_.node,
    limp.parsing.object_.node,
    limp.parsing.function.node,
    limp.parsing.function_call.node,
]
