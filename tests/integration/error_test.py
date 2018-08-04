import limp
import limp.errors as Errors
from nose.tools import *


def test_that_empty_code_raises_an_error():
    yield assert_raises, Errors.EmptyCode, limp.evaluate, ""


def test_that_invoking_nothing_raises_an_error():
    yield assert_raises, Errors.EmptyFunctionCall, limp.evaluate, "()"
