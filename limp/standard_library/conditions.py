CONDITION = 'condition'


def symbols():
    return {
        CONDITION: _condition,
    }


def _condition(entries):
    for entry in entries:
        if entry[0]:
            return entry[1]
