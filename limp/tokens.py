OPENING_PARENTHESIS = '('
CLOSING_PARENTHESIS = ')'
PARENTHESES = [OPENING_PARENTHESIS, CLOSING_PARENTHESIS]


def create_from(source_code):
    return _pad_characters(source_code, PARENTHESES).split()


def _pad_characters(source_code, characters):
    if characters == []:
        return source_code
    return _pad_characters(_pad(source_code, characters[0]), characters[1:])


def _pad(source_code, character):
    return source_code.replace(character, ' {} '.format(character))

