import operator


ARE_EQUAL =             "="
GREATER_THAN =          ">"
GREATER_THAN_OR_EQUAL = ">="
LESS_THAN =             "<"
LESS_THAN_OR_EQUAL =    "<="


def symbols():
    return {
        ARE_EQUAL:             operator.eq,
        GREATER_THAN:          operator.gt,
        LESS_THAN:             operator.lt,
        LESS_THAN_OR_EQUAL:    operator.le,
        GREATER_THAN_OR_EQUAL: operator.ge,
    }
