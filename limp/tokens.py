import limp.errors as Errors
import limp.parentheses as Parentheses
import re
from limp.types import *
from limp.utils import is_empty
from enum import Enum, auto, unique
from rply import LexerGenerator


@unique
class Types(Enum):
    Integer           = auto()
    Float             = auto()
    Binary            = auto()
    Octal             = auto()
    Hexadecimal       = auto()
    String            = auto()
    Symbol            = auto()
    OpenParenthesis   = auto()
    CloseParenthesis  = auto()
    FunctionDelimiter = auto()


def create_from(source_code):
    # _SanityChecks.not_empty(source_code)
    # _SanityChecks.no_unclosed_strings(source_code)
    # tokens = [token.value for token in _lexer().lex(source_code)]
    # _SanityChecks.parentheses_are_matched(tokens)
    return [(token.gettokentype(), token.value) for token in _lexer().lex(source_code)]


class _SanityChecks:

    @staticmethod
    def not_empty(source_code):
        if is_empty(source_code.strip()):
            raise Errors.EmptyCode()

    @staticmethod
    def no_unclosed_strings(source_code):
        string_delimiters = source_code.count(String.DELIMITER)
        if string_delimiters % 2 != 0:
            raise Errors.UnclosedString()

    @staticmethod
    def parentheses_are_matched(tokens):
        opening = tokens.count(Parentheses.OPEN)
        closing = tokens.count(Parentheses.CLOSE)

        def _raise_parenthesis_exception(greater, lesser, exception):
            difference = greater - lesser
            raise exception(difference)

        if closing > opening:
            _raise_parenthesis_exception(
                closing, opening, Errors.ExtraClosingParenthesis)
        elif opening > closing:
            _raise_parenthesis_exception(
                opening, closing, Errors.MissingClosingParenthesis)


def _lexer():
    generator = LexerGenerator()
    generator.ignore(_whitespace())

    token_regexes = [
        (Types.OpenParenthesis, re.escape(Parentheses.OPEN)),
        (Types.CloseParenthesis, re.escape(Parentheses.CLOSE)),
        (Types.FunctionDelimiter, re.escape(Function.KEYWORD)),
        (Types.Hexadecimal, _maybe_signed(f"{Hexadecimal.PREFIX}[\dA-Fa-f]+")),
        (Types.Octal, _maybe_signed(f"{Octal.PREFIX}[0-7]+")),
        (Types.Binary, _maybe_signed(f"{Binary.PREFIX}[01]+")),
        (Types.Float, _maybe_signed("\d*\.\d+")),
        (Types.Integer, _maybe_signed("\d+")),
        (Types.Symbol, _symbol_regex()),
        (Types.String, _string_regex()),
    ]

    for type_, regex in token_regexes:
        generator.add(type_, regex)

    return generator.build()


def _whitespace():
    return "\s+"


def _symbol_regex():
    ACCEPTABLE_CHARACTERS = "a-zA-Z_\-\?\!\=<>\+\*\/\%"
    return f"[{ACCEPTABLE_CHARACTERS}][0-9{ACCEPTABLE_CHARACTERS}]*"


def _string_regex():
    DELIMITER = re.escape(String.DELIMITER)
    return f"{DELIMITER}[^{DELIMITER}]*{DELIMITER}"

_maybe_signed = lambda number_regex: f"(\+|-)?{number_regex}"
