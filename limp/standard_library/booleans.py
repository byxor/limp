AND = "and"
OR = "or"
NOT = "not"
XOR = "xor"


def symbols():
    return {
        NOT: lambda a: not a,
        AND: lambda a, b: a and b,
        OR: lambda a, b: a or b,
        XOR: lambda a, b: (a and not b) or (b and not a)
    }
