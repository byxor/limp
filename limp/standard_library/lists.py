import limp.standard_library.shared as Shared
from functional import seq

APPEND_ELEMENT = "append"
PREPEND_ELEMENT = "prepend"
GET_ELEMENT = Shared.GET_ELEMENT
CONCATENATE = Shared.CONCATENATE
ALL_BUT_FIRST = Shared.ALL_BUT_FIRST
ALL_BUT_LAST = Shared.ALL_BUT_LAST
LENGTH = Shared.LENGTH
CONTAINS = Shared.CONTAINS
FIRST_ELEMENT = Shared.FIRST_ELEMENT
LAST_ELEMENT = Shared.LAST_ELEMENT
REVERSE = Shared.REVERSE
EMPTY = Shared.EMPTY
MAP = Shared.MAP
FILTER = Shared.FILTER
REDUCE = Shared.REDUCE


def symbols():
    return {
        REDUCE: lambda function, elements: seq(elements).reduce(function),
        GET_ELEMENT: lambda elements, index: elements[index],
        APPEND_ELEMENT: _append,
        PREPEND_ELEMENT: _prepend,
    }


def _append(elements, element):
    copy = elements[::]
    copy.append(element)
    return copy


def _prepend(elements, element):
    return [element] + elements
