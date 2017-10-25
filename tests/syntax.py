import limp.parentheses as Parentheses
import limp.types as Types


positive = lambda number_string: f'{Types.AbstractInteger.POSITIVE}{number_string}'
negative = lambda number_string: f'{Types.AbstractInteger.NEGATIVE}{number_string}'
integer = str
float_ = str
hexadecimal = hex
binary = bin
symbol = str


def object_(*attributes):
    KEYWORD = Types.Object.KEYWORD
    contents = [KEYWORD]
    for attribute in attributes:
        contents.append(form(*attribute))
    return form(*contents)


def list_of(*contents):
    KEYWORD = Types.List.KEYWORD
    return form(KEYWORD, *contents)


def shorthand_list_of(*contents):
    OPEN = Types.List.OPEN_DELIMITER
    CLOSE = Types.List.CLOSE_DELIMITER
    return f"{OPEN}{_space_separated(contents)}{CLOSE}"


def string(contents):
    DELIMITER = Types.String.DELIMITER
    return f'{DELIMITER}{contents}{DELIMITER}'


def boolean(value):
    TYPE = Types.Boolean
    return TYPE.TRUE_KEYWORD if value else TYPE.FALSE_KEYWORD


def if_statement(condition, main_body, else_body=""):
    return form(Types.SimpleConditional.KEYWORD, condition, main_body, else_body)


def conditional(*condition_value_pairs):
    KEYWORD = Types.ComplexConditional.KEYWORD
    contents = [KEYWORD]
    for pair in condition_value_pairs:
        contents.append(form(*pair))
    return form(*contents)


def invoke(function, *args):
    return form(function, *args)


def define(name, value):
    return form(Types.Definition.KEYWORD, name, value)


def function(parameter_names, body):
    PARAMETERS = parameters(parameter_names)
    return form(Types.Function.KEYWORD, PARAMETERS, body)


def shortened_function(body):
    return form(Types.Function.KEYWORD, body)


def shorthand_function(parameter_names, body):
    PARAMETERS = _space_separated(parameter_names)
    KEYWORD = Types.ShorthandFunction.KEYWORD
    code = form(PARAMETERS, KEYWORD, body)
    return code


def self_reference():
    return Types.Function.SELF_REFERENCE


def sequence(*args):
    KEYWORD = Types.SequentialEvaluator.KEYWORD
    return form(KEYWORD, *args)


def parameters(parameters):
    return form(*parameters)


def form(*code):
    return Parentheses.OPEN + _space_separated(code) + Parentheses.CLOSE


def _space_separated(strings):
    return " ".join(strings)
