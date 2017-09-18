import limp.parentheses as Parentheses
from collections import namedtuple


def create_from(tokens):
    algorithm_step = _create_algorithm_step_for(tokens, _START_INDEX)
    return _extract_token_tree_from(algorithm_step)


def _create_algorithm_step_for(tokens, start):
    tree = []
    index = start
    while index < len(tokens):
        token = tokens[index]
        if token == Parentheses.OPEN:
            algorithm_step = _create_algorithm_step_for(tokens, index + 1)
            tree.append(algorithm_step.tree)
            index = algorithm_step.next_index
        elif token == Parentheses.CLOSE:
            break
        else:
            tree.append(token)
        index += 1
    return _AlgorithmStep(tree, next_index=index)


def _extract_token_tree_from(algorithm_step):
    return algorithm_step.tree[0]


_AlgorithmStep = namedtuple('_InternalTree', 'tree next_index')
_START_INDEX = 0
