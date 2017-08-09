import limp.atom as atom
import limp.syntax as syntax


def create_from(tokens):
    SYNTAX_ERROR_MESSAGE = '{} while building Abstract Syntax Tree'
    if len(tokens) == 0:
        raise SyntaxError(SYNTAX_ERROR_MESSAGE.format('Unexpected EOF'))
    token = tokens.pop(0)
    if token == syntax.OPENING_PARENTHESIS:
        return _create_sub_tree_from(tokens)
    elif token == syntax.CLOSING_PARENTHESIS:
        raise SyntaxError(SYNTAX_ERROR_MESSAGE.format('Unexpected closing parenthesis'))
    else:
        return atom.create_from(token)


def _create_sub_tree_from(tokens):
    tree = []
    while tokens[0] != syntax.CLOSING_PARENTHESIS:
        tree.append(create_from(tokens))
    tokens.pop(0)
    return tree
