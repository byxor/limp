from functional import seq
import operator

CONCATENATE = "concatenate"
LENGTH = "length"
CONTAINS = "contains?"
GET_ELEMENT = "element"
FIRST_ELEMENT = "first"
LAST_ELEMENT = "last"
ALL_BUT_FIRST = "all-but-first"
ALL_BUT_LAST = "all-but-last"
REVERSE = "reverse"
EMPTY = "empty?"


def symbols():
    return {
        CONCATENATE: _concatenate,
        LENGTH: _length,
        CONTAINS: lambda a, b: b in a,
        FIRST_ELEMENT: lambda x: x[0],
        LAST_ELEMENT: lambda x: x[-1],
        ALL_BUT_FIRST: lambda x: x[1:],
        ALL_BUT_LAST: lambda x: x[:-1],
        REVERSE: lambda x: x[::-1],
        EMPTY: lambda x: len(x) == 0,
    }


def _concatenate(*args):
    first = args[0]
    second = args[1]
    all_but_first = args[1:]
    count = len(args)

    def _list_concatenate():
        concatenated = first[::]
        if count <= 2:
            for arg in second:
                concatenated.append(arg)
        else:
            for arg in all_but_first:
                concatenated.append(arg)
        return concatenated

    if isinstance(first, list):
        return _list_concatenate()
    else:
        return seq(args).map(str).reduce(operator.add)


def _length(x):
    return len(x)
