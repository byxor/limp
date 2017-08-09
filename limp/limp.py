import limp.environments as environments
import limp.syntax_tree as syntax_tree
import limp.tokens as tokens
import limp.types as types


def evaluate(syntax_tree, environment):
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
        environment[variable] = evaluate(expression, environment)
    else:
        procedure = evaluate(syntax_tree[0], environment)
        arguments = [evaluate(argument, environment) for argument in syntax_tree[1:]]
        return procedure(*arguments)

    
def parse(source_code):
    return syntax_tree.create_from(tokens.create_from(source_code))
    
