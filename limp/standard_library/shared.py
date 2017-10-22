from functional import seq
import operator


def symbols():
    return {
        'concatenate': _concatenate,
    }


def _concatenate(*args):
    first = args[0]
    second = args[1]
    all_but_first = args[1:]
    count = len(args)
    
    if type(first) == list:
        return _list_concatenate(count, first, second, all_but_first)
    else:
        return seq(args).map(str).reduce(operator.add)



def _list_concatenate(count, first, second, all_but_first):
    concatenated = first[::]
    if count <= 2:
        for arg in second:
            concatenated.append(arg)
    else:
        for arg in all_but_first:
            concatenated.append(arg)
    return concatenated
