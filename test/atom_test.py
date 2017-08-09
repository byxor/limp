import limp.atom as atom
import limp.types as types


def test_creation_from_values():
    data = [
        ('abc', 'abc', types.Symbol),
        ('def', 'def', types.Symbol),
        ('123', 123, int),
        ('456', 456, int),
        ('1.2', 1.2, float),
        ('2.4', 2.4, float)
    ]
    for symbol, expected_atom_value, expected_atom_type in data:
        atom_ = atom.create_from(symbol)
        assert atom_ ==  expected_atom_value
        assert type(atom_) == expected_atom_type

