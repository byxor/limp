import limp.types as types


def execute(syntax_tree, environment):
    if isinstance(syntax_tree, types.Symbol):
        symbol = syntax_tree
        try:
            return environment[symbol]
        except KeyError:
            raise NameError('Symbol "{}" is not defined'.format(symbol))
    elif not isinstance(syntax_tree, types.List):
        return syntax_tree
    elif syntax_tree[0] == 'define':
        (_, variable, expression) = syntax_tree
        environment[variable] = execute(expression, environment)
    else:
        procedure = execute(syntax_tree[0], environment)
        arguments = [execute(argument, environment) for argument in syntax_tree[1:]]
        return procedure(*arguments)
