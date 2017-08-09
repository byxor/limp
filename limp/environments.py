import limp.types as types
import operator


def create_standard():
    environment = types.Environment()
    environment.update({
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '//': operator.floordiv
    })
    return environment
