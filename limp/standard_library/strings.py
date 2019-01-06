import limp.environment as Environment
import limp.standard_library.shared as Shared

MODULE = "strings"
_method = lambda name: f"{MODULE}.{name}"

STRIP =     _method("strip")
REPEAT =    _method("repeat")
LOWERCASE = _method("lowercase")
UPPERCASE = _method("uppercase")
SPLIT =     _method("split")
JOIN =      _method("join")


def symbols():
    return {
        MODULE: {
            "join": lambda separator, list_: separator.join(map(str, list_)),
            "split": lambda delimiter, string: string.split(delimiter),
            "strip": lambda s: s.strip(),
            "lowercase": lambda s: s.lower(),
            "uppercase": lambda s: s.upper(),
            "repeat": lambda s, amount: s * amount,
            "split": lambda delimiter, string: string.split(delimiter),
        },
    }


EMPTY =         Shared.EMPTY
REVERSE =       Shared.REVERSE
CONCATENATE =   Shared.CONCATENATE
CONTAINS =      Shared.CONTAINS
LENGTH =        Shared.LENGTH
FIRST_ELEMENT = Shared.FIRST_ELEMENT
LAST_ELEMENT =  Shared.LAST_ELEMENT
ALL_BUT_FIRST = Shared.ALL_BUT_FIRST
ALL_BUT_LAST =  Shared.ALL_BUT_LAST
GET_ELEMENT =   Shared.GET_ELEMENT
MAP =           Shared.MAP
FILTER =        Shared.FILTER
