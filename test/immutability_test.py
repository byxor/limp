import limp
import limp.environment as Environment
from nose.tools import assert_equal


def test_lists_are_immutable():
    LIST_NAME = 'my-list'

    environment = Environment.create_standard()
    run = lambda source_code: limp.evaluate(source_code, environment)

    run(f'(define {LIST_NAME} (list 1 2 3))')
    list_before = environment.resolve(LIST_NAME)

    run(f'(append {LIST_NAME} 1)')
    run(f'(concatenate {LIST_NAME} (list 1 2 3))')
    run(f'(map {LIST_NAME} (function (n) (+ n 1)))')
    run(f'(filter {LIST_NAME} (function (x) (= x 1)))')
    run(f'(reduce {LIST_NAME} (function (a b) (+ a b)))')
    run(f'(first {LIST_NAME})')
    run(f'(last {LIST_NAME})')
    run(f'(all-but-first {LIST_NAME})')
    run(f'(all-but-last {LIST_NAME})')

    list_after = environment.resolve(LIST_NAME)

    yield assert_equal, list_before, list_after
