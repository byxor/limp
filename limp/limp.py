import limp.environments as environments
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
    return build_syntax_tree(tokens.create_from(source_code))


def build_syntax_tree(tokens_):
    SYNTAX_ERROR_MESSAGE = '{} while building Abstract Syntax Tree'
    if len(tokens_) == 0:
        raise SyntaxError(SYNTAX_ERROR_MESSAGE.format('Unexpected EOF'))
    token = tokens_.pop(0)
    if token == tokens.OPENING_PARENTHESIS:
        return _build_sub_syntax_tree(tokens_)
    elif token == tokens.CLOSING_PARENTHESIS:
        raise SyntaxError(SYNTAX_ERROR_MESSAGE.format('Unexpected closing parenthesis'))
    else:
        return atomize(token)


def atomize(symbol):
    if _represents(symbol, int):
        return int(symbol)
    elif _represents(symbol, float):
        return float(symbol)
    else:
        return types.Symbol(symbol)

    
def _represents(symbol, type_):
    try:
        type_(symbol)
        return True
    except ValueError:
        return False

    
def _build_sub_syntax_tree(tokens_):
    tree = []
    while tokens_[0] != tokens.CLOSING_PARENTHESIS:
        tree.append(build_syntax_tree(tokens_))
    tokens_.pop(0)
    return tree    

