IF = 'if'


def symbols():
    return {
        IF: _if,
    }


def _if(condition, value_if_true, value_if_false=None):
    if condition:
        return value_if_true
    else:
        return value_if_false
