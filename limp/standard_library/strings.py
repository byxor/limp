import limp.standard_library.shared as Shared


STRIP =       "strip"
REPEAT =      "repeat"
LOWERCASE =   "lowercase"
UPPERCASE =   "uppercase"
SPLIT =       "split"
JOIN =        "join-string"

EMPTY =       "empty?"
REVERSE =     "reverse"

CONCATENATE = Shared.CONCATENATE
CONTAINS =    Shared.CONTAINS
LENGTH =      Shared.LENGTH


def symbols():
    return {
        STRIP:     lambda s: s.strip(),
        LOWERCASE: lambda s: s.lower(),
        UPPERCASE: lambda s: s.upper(),
        REPEAT:    lambda s, amount: s * amount,
        SPLIT:     lambda delimiter, string: string.split(delimiter),
        JOIN:      lambda separator, list_: separator.join(list_),
        
        EMPTY:     lambda s: len(s) == 0,
        REVERSE:   lambda s: s[::-1],
    }
