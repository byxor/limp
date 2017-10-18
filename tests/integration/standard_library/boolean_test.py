import tests.helpers as Helpers
from tests.syntax import *


NOT = "not"
AND = "and"
OR =  "or"
XOR = "xor"


def test():
    Helpers.run_evaluation_test_on([
        (invoke(NOT, boolean(True)), False),
        (invoke(NOT, boolean(False)), True),

        (invoke(AND, boolean(True), boolean(True)),   True),
        (invoke(AND, boolean(True), boolean(False)),  False),
        (invoke(AND, boolean(False), boolean(True)),  False),
        (invoke(AND, boolean(False), boolean(False)), False),

        (invoke(OR, boolean(True), boolean(True)),   True),
        (invoke(OR, boolean(True), boolean(False)),  True),
        (invoke(OR, boolean(False), boolean(True)),  True),
        (invoke(OR, boolean(False), boolean(False)), False),

        (invoke(XOR, boolean(True), boolean(True)),   False),
        (invoke(XOR, boolean(True), boolean(False)),  True),
        (invoke(XOR, boolean(False), boolean(True)),  True),
        (invoke(XOR, boolean(False), boolean(False)), False),
    ])
