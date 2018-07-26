import limp.syntax as Syntax

STRING = "string"
INTEGER = "integer"
FLOAT = "float"
BOOLEAN = "boolean"


def symbols():
    return {
        INTEGER: int,
        STRING: str,
        FLOAT: float,
        BOOLEAN: _boolean,
    }


def _boolean(x):
    if isinstance(x, str):
        return x == Syntax.TRUE
    else:
        return bool(x)
