import limp.syntax_tree as SyntaxTree


def evaluate(tree, environment):
    type_ = tree[0]
    evaluator = _evaluators[type_]
    return evaluator(tree, environment)


_TreeTypes = SyntaxTree.Types


def _evaluate_function_call(tree, environment):
    print("EVALUATE_FUNCTION_CALL")
    function = evaluate(tree[1], environment)
    parameter_values = [evaluate(t, environment) for t in tree[2]]
    return function(*parameter_values)


def _evaluate_function(tree, environment):
    print("EVALUATE_FUNCTION")
    parameter_names = [t[1] for t in tree[1]]

    def internal_function(*parameter_values):
        execution_environment = environment.new_child()
        parameters = zip(parameter_names, parameter_values)

        for name, value in parameters:
            execution_environment.define(name, value)

        output = evaluate(tree[2], execution_environment)
        return output

    return internal_function


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
    _TreeTypes.FunctionCall:  _evaluate_function_call,
    _TreeTypes.Function:      _evaluate_function,
}
