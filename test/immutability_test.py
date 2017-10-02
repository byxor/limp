import limp
import limp.environment as Environment
from nose.tools import assert_equal


def test_lists_are_immutable():
    LIST_NAME = 'my-list'
    LIST_VALUE = [1, 2, 3]

    environment = Environment.create_standard()
    environment.define(LIST_NAME, LIST_VALUE)
    
    run = lambda source_code: limp.evaluate(source_code, environment)

    run(f'(append {LIST_NAME} 1)')
    run(f'(concatenate {LIST_NAME} (list 1 2 3))')
    run(f'(map {LIST_NAME} (function (n) (+ n 1)))')
    run(f'(filter {LIST_NAME} (function (x) (= x 1)))')
    run(f'(reduce {LIST_NAME} (function (a b) (+ a b)))')
    run(f'(first {LIST_NAME})')
    run(f'(last {LIST_NAME})')
    run(f'(all-but-first {LIST_NAME})')
    run(f'(all-but-last {LIST_NAME})')

    yield assert_equal, LIST_VALUE, environment.resolve(LIST_NAME)
