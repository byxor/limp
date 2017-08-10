import limp.types as Types
import operator


def create_standard():
    environment = Types.Environment()
    environment.update({
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '//': operator.floordiv
    })
    return environment
