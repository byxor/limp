import limp.tokens as tokens
import limp


def create_from(tokens_):
    SYNTAX_ERROR_MESSAGE = '{} while building Abstract Syntax Tree'
    if len(tokens_) == 0:
        raise SyntaxError(SYNTAX_ERROR_MESSAGE.format('Unexpected EOF'))
    token = tokens_.pop(0)
    if token == tokens.OPENING_PARENTHESIS:
        return _build_sub_syntax_tree(tokens_)
    elif token == tokens.CLOSING_PARENTHESIS:
        raise SyntaxError(SYNTAX_ERROR_MESSAGE.format('Unexpected closing parenthesis'))
    else:
        return limp.limp.atomize(token)


def _build_sub_syntax_tree(tokens_):
    tree = []
    while tokens_[0] != tokens.CLOSING_PARENTHESIS:
        tree.append(create_from(tokens_))
    tokens_.pop(0)
    return tree
