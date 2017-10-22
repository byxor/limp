import limp.standard_library.shared as Shared
from functional import seq


MAP =             "map"
FILTER =          "filter"
REDUCE =          "reduce"
GET_ELEMENT =     "element"
APPEND_ELEMENT =  "append"
PREPEND_ELEMENT = "prepend"
CONCATENATE =     "concatenate"
FIRST_ELEMENT =   "first"
LAST_ELEMENT =    "last"
ALL_BUT_FIRST =   "all-but-first"
ALL_BUT_LAST =    "all-but-last"
LENGTH =          Shared.LENGTH
CONTAINS =        Shared.CONTAINS


def symbols():
    return {
        MAP:             lambda function, elements: seq(elements).map(function),
        FILTER:          lambda function, elements: seq(elements).filter(function),
        REDUCE:          lambda function, elements: seq(elements).reduce(function),
        GET_ELEMENT:     lambda elements, index: elements[index],
        APPEND_ELEMENT:  _append,
        PREPEND_ELEMENT: _prepend,
        FIRST_ELEMENT:   lambda elements: elements[0],
        LAST_ELEMENT:    lambda elements: elements[-1],
        ALL_BUT_FIRST:   lambda elements: elements[1:],
        ALL_BUT_LAST:    lambda elements: elements[:-1],
    }


def _append(elements, element):
    copy = elements[::]
    copy.append(element)
    return copy


def _prepend(elements, element):
    return [element] + elements
