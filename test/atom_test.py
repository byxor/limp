import limp.atom as Atom
import limp.types as Types


def test_creation_from_values():
    data = [
        ('abc', 'abc', Types.Symbol),
        ('def', 'def', Types.Symbol),
        ('123', 123, int),
        ('456', 456, int),
        ('1.2', 1.2, float),
        ('2.4', 2.4, float),
        ('0x5', 0x5, int),
        ('0xABC', 0xABC, int),
        ('0b1', 0b1, int),
        ('0b101011', 0b101011, int)
    ]
    for symbol, expected_value, expected_type in data:
        atom = Atom.create_from(symbol)
        assert atom == expected_value
        assert type(atom) == expected_type
