import limp.types as Types


def create_from(symbol):
    if _represents(symbol, int):
        return int(symbol)
    elif _represents(symbol, float):
        return float(symbol)
    else:
        return Types.Symbol(symbol)

    
def _represents(symbol, type_):
    try:
        type_(symbol)
        return True
    except ValueError:
        return False
