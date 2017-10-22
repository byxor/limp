def symbols():
    return {
        'not': lambda a: not a,
        'and': lambda a, b: a and b,
        'or':  lambda a, b: a or b,
        'xor': lambda a, b: (a and not b) or (b and not a)
    }
