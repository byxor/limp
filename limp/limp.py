import operator

OPENING_PARENTHESIS = '('
CLOSING_PARENTHESIS = ')'
PARENTHESES = [OPENING_PARENTHESIS, CLOSING_PARENTHESIS]

Symbol = str
List = list
Number = (int, float)
Environment = dict


def standard_environment():
    environment = Environment()
    environment.update({
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '//': operator.floordiv
    })
    return environment


def evaluate(syntax_tree, environment):
    if isinstance(syntax_tree, Symbol):
        symbol = syntax_tree
        try:
            return environment[symbol]
        except KeyError:
            raise NameError('Symbol "{}" is not defined'.format(symbol))
    elif not isinstance(syntax_tree, List):
        return syntax_tree
    elif syntax_tree[0] == 'define':
        (_, variable, expression) = syntax_tree
        environment[variable] = evaluate(expression, environment)
    else:
        procedure = evaluate(syntax_tree[0], environment)
        arguments = [evaluate(argument, environment) for argument in syntax_tree[1:]]
        return procedure(*arguments)

    
def parse(source_code):
    return build_syntax_tree(tokenize(source_code))


def build_syntax_tree(tokens):
    SYNTAX_ERROR_MESSAGE = '{} while building Abstract Syntax Tree'
    if len(tokens) == 0:
        raise SyntaxError(SYNTAX_ERROR_MESSAGE.format('Unexpected EOF'))
    token = tokens.pop(0)
    if token == OPENING_PARENTHESIS:
        return _build_sub_syntax_tree(tokens)
    elif token == CLOSING_PARENTHESIS:
        raise SyntaxError(SYNTAX_ERROR_MESSAGE.format('Unexpected closing parenthesis'))
    else:
        return atomize(token)

    
def tokenize(source_code):
    return _pad_characters(source_code, PARENTHESES).split()


def atomize(symbol):
    if _represents(symbol, int):
        return int(symbol)
    elif _represents(symbol, float):
        return float(symbol)
    else:
        return Symbol(symbol)

    
def _represents(symbol, type_):
    try:
        type_(symbol)
        return True
    except ValueError:
        return False

    
def _build_sub_syntax_tree(tokens):
    tree = []
    while tokens[0] != CLOSING_PARENTHESIS:
        tree.append(build_syntax_tree(tokens))
    tokens.pop(0)
    return tree    


def _pad_characters(source_code, characters):
    if characters == []:
        return source_code
    return _pad_characters(_pad(source_code, characters[0]), characters[1:])


def _pad(source_code, character):
    return source_code.replace(character, ' {} '.format(character))


