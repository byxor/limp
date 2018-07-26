import limp.environment as Environment
import limp.errors as Errors
from nose.tools import *
from tests.syntax import *


ARBITRARY_NAME = "x"


def test_defining_symbols():
    environment = Environment.create_empty()
    data = [
        ('x', 0),
        ('y', 1),
        ('z', 2),
    ]
    for name, expected_value in data:
        environment.define(name, expected_value)
        value = environment.resolve(name)
        yield assert_equal, expected_value, value


def test_creating_child_environments():
    parent_value = "parent"
    child_value = "child"

    parent = Environment.create_empty()
    parent.define(ARBITRARY_NAME, parent_value)

    child = parent.new_child()
    yield assert_equal, parent_value, child.resolve(ARBITRARY_NAME)
    child.define(ARBITRARY_NAME, child_value)
    yield assert_equal, child_value, child.resolve(ARBITRARY_NAME)
    yield assert_equal, parent_value, parent.resolve(ARBITRARY_NAME)


def test_error_thrown_when_defining_existing_symbol():
    environment = Environment.create_empty()
    environment.define(ARBITRARY_NAME, 10)
    yield assert_raises, Errors.RedefinedSymbol, environment.define, ARBITRARY_NAME, 20
    


def test_string_representation():
    symbols = [
        ('name_a', 10),
        ('name_b', 20),
    ]

    environment = Environment.create_empty()
    for name, value in symbols:
        environment.define(name, value)

    representation = str(environment)

    for name, value in symbols:
        expected_substrings = [str(x) for x in [name, value]]
        for substring in expected_substrings:
            yield assert_in, substring, representation
