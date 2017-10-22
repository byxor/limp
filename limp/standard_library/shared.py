from functional import seq
import operator


CONCATENATE = "concatenate"
LENGTH =      "length"
CONTAINS =    "contains"


def symbols():
    return {
        CONCATENATE: _concatenate,
        LENGTH:      _length,
        CONTAINS:    lambda a, b: b in a,
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

    if type(first) == list:
        return _list_concatenate()
    else:
        return seq(args).map(str).reduce(operator.add)





def _length(x): return len(x)
