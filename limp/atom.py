import limp.types as Types


def create_from(token):
    types = [int, float, Types.HexadecimalType, Types.BinaryType, Types.Symbol]
    for type_ in types:
        if _represents(token, type_):
            return type_(token)

    
def _represents(token, type_):
    try:
        type_(token)
        return True
    except ValueError:
        return False


