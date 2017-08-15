import limp.atom as Atom
import limp.parentheses as Parentheses


def create_from(tokens):
    _assert_not_empty(tokens)
    _assert_parentheses_are_matched(tokens)

    first_token = tokens.pop(0)
    token_begins_new_form = lambda: first_token == Parentheses.OPEN
    
    if token_begins_new_form():
        return _create_form_from(tokens)
    else:
        return Atom.create_from(first_token)


def _create_form_from(tokens):
    create_syntax_tree_from = create_from
    form = []
    while tokens[0] != Parentheses.CLOSE:
        sub_tree = create_syntax_tree_from(tokens)
        form.append(sub_tree)
    tokens.pop(0)
    return form
    

def _assert_not_empty(tokens):
    if len(tokens) == 0:
        raise SyntaxError(_ERROR_MESSAGE.format('Unexpected EOF'))


def _assert_parentheses_are_matched(tokens):
    if tokens[0] == Parentheses.CLOSE:
        raise SyntaxError(_ERROR_MESSAGE.format('Unexpected closing parenthesis'))


_ERROR_MESSAGE = '{} while building Abstract Syntax Tree'
