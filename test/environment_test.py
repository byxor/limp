import limp.environment as Environment
from nose.tools import assert_equal


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
    name = 'x'
    parent_value = "parent"
    child_value = "child"
    
    parent = Environment.create_empty()
    parent.define(name, parent_value)
    
    child = parent.new_child()
    yield assert_equal, parent_value, child.resolve(name)
    child.define(name, child_value)
    yield assert_equal, child_value, child.resolve(name)
    yield assert_equal, parent_value, parent.resolve(name)
    
    
