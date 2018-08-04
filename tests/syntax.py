import limp.syntax as Syntax


positive = lambda number_string: f'{Syntax.POSITIVE}{number_string}'
negative = lambda number_string: f'{Syntax.NEGATIVE}{number_string}'
integer = str
float_ = str
hexadecimal = hex
binary = bin
octal = oct
symbol = str


def list_of(*contents):
    return f"{Syntax.OPEN_LIST}{_space_separated(contents)}{Syntax.CLOSE_LIST}"


def string(contents):
    return f'{Syntax.STRING_DELIMITER}{contents}{Syntax.STRING_DELIMITER}'


def boolean(value):
    return Syntax.TRUE if value else Syntax.FALSE


def conditional(*pairs):
    code = f'{Syntax.CONDITIONAL} {{ '
    for condition, return_value in pairs:
        code += f"{condition}:{return_value} "
    code += '}'
    return code


def invoke(function, *args):
    return form(function, *args)


def function(parameter_names, body):
    return _function(Syntax.FUNCTION_DELIMITER, parameter_names, body)


def _function(keyword, parameter_names, body):
    PARAMETERS = _space_separated(parameter_names)
    code = form(PARAMETERS, keyword, body)
    return code


def self_reference():
    return Syntax.SELF_REFERENCE


def form(*code):
    return Syntax.OPEN_EXPRESSION + _space_separated(code) + Syntax.CLOSE_EXPRESSION


def _space_separated(strings):
    return " ".join(strings)
