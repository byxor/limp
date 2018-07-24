import limp.errors as Errors
import limp.parentheses as Parentheses
import re
from limp.types import *
from limp.utils import is_empty
from rply import LexerGenerator
from collections import namedtuple
from enum import Enum, auto, unique


Token = namedtuple('Token', 'type_ contents')


def create_from(source_code):
    return [Token(token.gettokentype(), token.value) for token in _lex(source_code)]


def _lex(source_code):
    generator = LexerGenerator()
    generator.ignore("\s+")

    for matcher in _matchers():
        generator.add(*matcher)

    lexer = generator.build()
    return lexer.lex(source_code)


def _matchers():
    return [
        (Types.OpenParenthesis, re.escape(Parentheses.OPEN)),
        (Types.CloseParenthesis, re.escape(Parentheses.CLOSE)),
        (Types.OpenSquareBracket, re.escape("[")),
        (Types.CloseSquareBracket, re.escape("]")),
        (Types.FunctionDelimiter, re.escape(Function.KEYWORD)),
        (Types.Hexadecimal, _maybe_signed(f"{Hexadecimal.PREFIX}[\dA-Fa-f]+")),
        (Types.Octal, _maybe_signed(f"{Octal.PREFIX}[0-7]+")),
        (Types.Binary, _maybe_signed(f"{Binary.PREFIX}[01]+")),
        (Types.Float, _maybe_signed("\d*\.\d+")),
        (Types.Integer, _maybe_signed("\d+")),
        (Types.Symbol, _symbol_regex()),
        (Types.String, _string_regex()),
    ]


@unique
class Types(Enum):
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
    DELIMITER = re.escape(String.DELIMITER)
    return f"{DELIMITER}[^{DELIMITER}]*{DELIMITER}"

_maybe_signed = lambda number_regex: f"(\+|-)?{number_regex}"

