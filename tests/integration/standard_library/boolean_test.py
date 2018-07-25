import tests.helpers as Helpers
from tests.syntax import *
from limp.standard_library.booleans import *


_ = Helpers.evaluation_fixture("test", [
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
