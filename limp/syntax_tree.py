import limp.atom as Atom
import limp.parentheses as Parentheses


def create_from(tokens):
    SYNTAX_ERROR_MESSAGE = '{} while building Abstract Syntax Tree'
    if len(tokens) == 0:
        raise SyntaxError(SYNTAX_ERROR_MESSAGE.format('Unexpected EOF'))
    token = tokens.pop(0)
    if token == Parentheses.OPEN:
        return _create_sub_tree_from(tokens)
    elif token == Parentheses.CLOSE:
        raise SyntaxError(SYNTAX_ERROR_MESSAGE.format('Unexpected closing parenthesis'))
    else:
        return Atom.create_from(token)


def _create_sub_tree_from(tokens):
    tree = []
    while tokens[0] != Parentheses.CLOSE:
        tree.append(create_from(tokens))
    tokens.pop(0)
    return tree
