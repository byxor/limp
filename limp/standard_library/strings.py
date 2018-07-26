import limp.standard_library.shared as Shared

STRIP = "strip"
REPEAT = "repeat"
LOWERCASE = "lowercase"
UPPERCASE = "uppercase"
SPLIT = "split"
JOIN = "join-string"

EMPTY = Shared.EMPTY
REVERSE = Shared.REVERSE
CONCATENATE = Shared.CONCATENATE
CONTAINS = Shared.CONTAINS
LENGTH = Shared.LENGTH
FIRST_ELEMENT = Shared.FIRST_ELEMENT
LAST_ELEMENT = Shared.LAST_ELEMENT
ALL_BUT_FIRST = Shared.ALL_BUT_FIRST
ALL_BUT_LAST = Shared.ALL_BUT_LAST
GET_ELEMENT = Shared.GET_ELEMENT


def symbols():
    return {
        STRIP: lambda s: s.strip(),
        LOWERCASE: lambda s: s.lower(),
        UPPERCASE: lambda s: s.upper(),
        REPEAT: lambda s, amount: s * amount,
        SPLIT: lambda delimiter, string: string.split(delimiter),
        JOIN: lambda separator, list_: separator.join(list_),
    }
