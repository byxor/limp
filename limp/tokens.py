import limp.errors as Errors
import limp.syntax as Syntax
import re
from rply import LexerGenerator
from collections import namedtuple
from enum import Enum, auto, unique


Token = namedtuple('Token', 'type_ contents')


def create_from(source_code):
    return [Token(token.gettokentype(), token.value) for token in _lex(source_code)]


def _lex(source_code):
    generator = LexerGenerator()
    _ignore_whitespace(generator)

    for matcher in _matchers():
        generator.add(*matcher)

    lexer = generator.build()
    return lexer.lex(source_code)


def _ignore_whitespace(generator):
    generator.ignore("\s+")


def _matchers():
    return [
        (Types.OpenParenthesis, re.escape('(')),
        (Types.CloseParenthesis, re.escape(')')),
        (Types.OpenSquareBracket, re.escape('[')),
        (Types.CloseSquareBracket, re.escape(']')),
        (Types.FunctionDelimiter, re.escape(Syntax.FUNCTION_DELIMITER)),
        (Types.Hexadecimal, _maybe_signed(f"{Syntax.HEXADECIMAL_PREFIX}[\dA-Fa-f]+")),
        (Types.Octal, _maybe_signed(f"{Syntax.OCTAL_PREFIX}[0-7]+")),
        (Types.Binary, _maybe_signed(f"{Syntax.BINARY_PREFIX}[01]+")),
        (Types.Float, _maybe_signed("\d*\.\d+")),
        (Types.Integer, _maybe_signed("\d+")),
        (Types.Boolean, "false\\b|true\\b"),
        (Types.Symbol, _symbol_regex()),
        (Types.String, _string_regex()),
    ]


@unique
class Types(Enum):
    Boolean            = auto()
    Integer            = auto()
    Float              = auto()
    Binary             = auto()
    Octal              = auto()
    Hexadecimal        = auto()
    String             = auto()
    Symbol             = auto()
    OpenParenthesis    = auto()
    CloseParenthesis   = auto()
    FunctionDelimiter  = auto()
    OpenSquareBracket  = auto()
    CloseSquareBracket = auto()


def _symbol_regex():
    ACCEPTABLE_CHARACTERS = "a-zA-Z_\-\?\!\=<>\+\*\/\%"
    return f"[{ACCEPTABLE_CHARACTERS}][0-9{ACCEPTABLE_CHARACTERS}]*"


def _string_regex():
    DELIMITER = re.escape(Syntax.STRING_DELIMITER)
    return f"{DELIMITER}[^{DELIMITER}]*{DELIMITER}"

_maybe_signed = lambda number_regex: f"(\+|-)?{number_regex}"

