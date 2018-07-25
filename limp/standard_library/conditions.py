IF        = 'if'
CONDITION = 'condition'


def symbols():
    return {
        IF:        _if,
        CONDITION: _condition,
    }


def _if(condition, value_if_true, value_if_false=None):
    if condition:
        return value_if_true
    else:
        return value_if_false


def _condition(entries):
    for entry in entries:
        if entry[0]:
            return entry[1]
