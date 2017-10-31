import tests.helpers as Helpers
from tests.syntax import *


def test_numeric_types():
    Helpers.run_evaluation_test_on([
        (integer(0),           0),
        (integer(10),          10),
        (integer(23),          23),
        (negative(integer(4)), -4),
        (positive(integer(4)), +4),

        (hexadecimal(0x0),               0x0),
        (hexadecimal(0x123),             0x123),
        (hexadecimal(0xDEADA55),         0xDEADA55),
        (negative(hexadecimal(0x1)),     -0x1),
        (negative(hexadecimal(0xBEEF)),  -0xBEEF),
        (positive(hexadecimal(0xB00B5)), +0xB00B5),

        (binary(0b0),              0b0),
        (binary(0b1),              0b1),
        (binary(0b101),            0b101),
        (negative(binary(0b1)),    -0b1),
        (negative(binary(0b111)),  -0b111),
        (positive(binary(0b10)),   +0b10),

        (octal(0o0),              0o0),
        (octal(0o1),              0o1),
        (octal(0o4234),           0o4234),
        (negative(octal(0o1)),    -0o1),
        (negative(octal(0o4536)), -0o4536),
        (positive(octal(0o42)),   +0o42),

        (float_(0),               0.0),
        (float_(0.5),             0.5),
        (float_(2.3),             2.3),
        (float_(1.23456789),      1.23456789),
        (negative(float_(2.5)),   -2.5),
        (negative(float_(60.12)), -60.12),
        (positive(float_(20.3)),  +20.3),
    ])


def test_booleans():
    Helpers.run_evaluation_test_on([
        (boolean(True),  True),
        (boolean(False), False),
    ])


def test_strings():
    Helpers.run_evaluation_test_on([
        (string("Hey"),          "Hey"),
        (string("Hello there!"), "Hello there!"),
        (string("\n\n\n"),       "\n\n\n"),
    ])

