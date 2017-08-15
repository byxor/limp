def _create_integer_type(base, prefix):
    def ExternalType(token):
        def _has_prefix(): return token.startswith(prefix)
        def _conversion_function(): return int(token, base)
        if _has_prefix():
            return _conversion_function()
        else:
            raise ValueError()
    return ExternalType


Symbol = str
List = list
Environment = dict
BinaryType = _create_integer_type(2, '0b')
HexadecimalType = _create_integer_type(16, '0x')

