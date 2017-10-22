def symbols():
    return {
        'strip':       lambda s: s.strip(),
        'empty?':      lambda s: len(s) == 0, 
        'contains?':   lambda a, b: b in a,
        'repeat':      lambda s, amount: s * amount,
        'reverse':     lambda s: s[::-1],
        'lowercase':   lambda s: s.lower(),
        'uppercase':   lambda s: s.upper(),
        'split':       lambda delimiter, string: string.split(delimiter),
        'join-string': lambda separator, list_: separator.join(list_),
    }
