import limp.atom as Atom
import limp.types as Types


def test_creation_from_values():
    data = [
        ('abc', 'abc', Types.Symbol),
        ('def', 'def', Types.Symbol),
        ('123', 123, int),
        ('456', 456, int),
        ('1.2', 1.2, float),
        ('2.4', 2.4, float)
    ]
    for symbol, expected_atom_value, expected_atom_type in data:
        atom = Atom.create_from(symbol)
        assert atom ==  expected_atom_value
        assert type(atom) == expected_atom_type

