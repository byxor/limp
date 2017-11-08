STRING =  "string"
INTEGER = "integer"
FLOAT =   "float"
BOOLEAN = "boolean"


def symbols():
    return {
        INTEGER: int,
        STRING:  str,
        FLOAT:   float,
        BOOLEAN: _boolean,
    }


def _boolean(x):
    if isinstance(x, str):
        import limp.types as Types
        return x == Types.Boolean.TRUE_KEYWORD
    else:
        return bool(x)
