import limp.types as Types


def create_from(token):
    if _represents(token, int):
        return int(token)
    elif _represents(token, float):
        return float(token)
    elif _represents_hexadecimal(token):
        return int(token, 16)
    else:
        return Types.Symbol(token)

    
def _represents(token, type_):
    try:
        type_(token)
        return True
    except ValueError:
        return False


def _represents_hexadecimal(token):
    hexadecimal_type = lambda value: int(value, 16)
    is_parseable = _represents(token, hexadecimal_type)
    hexadecimal_prefix = '0x'
    return is_parseable and token.startswith(hexadecimal_prefix)

