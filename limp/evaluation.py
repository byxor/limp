import limp.syntax_tree as SyntaxTree


def evaluate(tree, environment):
    type_ = tree[0]
    evaluator = _evaluators[type_]
    return evaluator(tree, environment)


_TreeTypes = SyntaxTree.Types


def _function_call(tree, environment):
    function = evaluate(tree[1], environment)
    arguments = [evaluate(t, environment) for t in tree[2]]
    return function(*arguments)


_evaluators = {
    _TreeTypes.Boolean:       lambda tree, environment: tree[1] == "true",
    _TreeTypes.Float:         lambda tree, environment: float(tree[1]),
    _TreeTypes.Integer:       lambda tree, environment: int(tree[1]),
    _TreeTypes.Binary:        lambda tree, environment: int(tree[1], 2),
    _TreeTypes.Octal:         lambda tree, environment: int(tree[1], 8),
    _TreeTypes.Hexadecimal:   lambda tree, environment: int(tree[1], 16),
    _TreeTypes.UnaryNegative: lambda tree, environment: -(evaluate(tree[1], environment)),
    _TreeTypes.UnaryPositive: lambda tree, environment: evaluate(tree[1], environment),
    _TreeTypes.String:        lambda tree, environment: tree[1][1:-1],
    _TreeTypes.Symbol:        lambda tree, environment: environment.resolve(tree[1]),
    _TreeTypes.List:          lambda tree, environment: [evaluate(t, environment) for t in tree[1]],
    _TreeTypes.FunctionCall:  _function_call,
}
