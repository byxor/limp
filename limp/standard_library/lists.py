from functional import seq


def symbols():
    return {
        'map':           lambda function, elements: seq(elements).map(function),
        'filter':        lambda function, elements: seq(elements).filter(function),
        'reduce':        lambda function, elements: seq(elements).reduce(function),
        'element':       lambda elements, index: elements[index],
        'append':        _append,
        'prepend':       _prepend,
        'first':         lambda elements: elements[0],
        'last':          lambda elements: elements[-1],
        'all-but-first': lambda elements: elements[1:],
        'all-but-last':  lambda elements: elements[:-1],
    }


def _append(elements, element):
    copy = elements[::]
    copy.append(element)
    return copy


def _prepend(elements, element):
    return [element] + elements
