def symbols():
    return {
        'integer': int,
        'string':  str,
        'float':   float,
        'boolean': _boolean,
    }


def _boolean(x):
    if type(x) == str:
        import limp.types as Types
        return x == Types.Boolean.TRUE_KEYWORD
    else:
        return bool(x)

