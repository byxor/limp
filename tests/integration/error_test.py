import limp
import limp.errors as Errors
from nose.tools import *


def test_that_empty_code_raises_an_error():
    yield assert_raises, Errors.EmptyCode, limp.evaluate, ""


# Function Calls

def test_that_calling_nothing_raises_an_error():
    yield assert_raises, Errors.EmptyFunctionCall, limp.evaluate, "()"


# Strings

def test_that_unclosed_strings_raise_errors():
    yield assert_raises, Errors.UnclosedString, limp.evaluate, '"foo'


# Objects

def test_that_objects_need_the_correct_number_of_elements():
    data = [
        "{foo:bar baz bliz}"
        "{foo bar}",
    ]
    for source_code in data:
        yield assert_raises, Errors.MalformedObject, limp.evaluate, source_code


def test_that_objects_delimiters_must_be_delimiters():
    data = [
        '{foo o baz}',
        '{foo: bar  baz "" bliz}',
    ]
    for source_code in data:
        yield assert_raises, Errors.IncorrectObjectDelimiter, limp.evaluate, source_code
