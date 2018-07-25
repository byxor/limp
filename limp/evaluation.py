import limp.syntax_tree as SyntaxTree


def evaluate(tree):
    type_ = tree[0]
    evaluator = _evaluators[type_]
    return evaluator(tree)


_TreeTypes = SyntaxTree.Types


_evaluators = {
    _TreeTypes.Integer:       lambda tree: int(tree[1]),
    _TreeTypes.Binary:        lambda tree: int(tree[1], 2),
    _TreeTypes.Hexadecimal:   lambda tree: int(tree[1], 16),
    _TreeTypes.UnaryNegative: lambda tree: -(evaluate(tree[1])),
    _TreeTypes.UnaryPositive: lambda tree: evaluate(tree[1]),
}
