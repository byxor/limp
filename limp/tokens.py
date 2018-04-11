import limp.errors as Errors
import limp.parentheses as Parentheses
import re
from limp.types import *
from limp.utils import is_empty
from rply import LexerGenerator


def create_from(source_code):
    _SanityChecks.not_empty(source_code)
    _SanityChecks.no_unclosed_strings(source_code)
    tokens = [token.value for token in _lexer().lex(source_code)]
    _SanityChecks.parentheses_are_matched(tokens)
    return tokens


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
        *_simple_delimiters_and_tokens(),
        *_numeric_literals(),
        _symbols(),
        _strings(),
    ]

    for regex in token_regexes:
        generator.add("", regex)

    return generator.build()


def _whitespace():
    return "\s+"


def _simple_delimiters_and_tokens():
    return [
        re.escape(Parentheses.OPEN),
        re.escape(Parentheses.CLOSE),
        re.escape(Function.KEYWORD),
    ]


def _symbols():
    ACCEPTABLE_CHARACTERS = "a-zA-Z_\-\?\!\=<>\+\*\/\%"
    return f"[{ACCEPTABLE_CHARACTERS}][0-9{ACCEPTABLE_CHARACTERS}]*"


def _numeric_literals():
    _maybe_signed = lambda number_regex: f"(\+|-)?{number_regex}"

    INTEGERS_OR_FLOATS = _maybe_signed("([\d]+)(\.[\d]+)?")
    HEXADECIMAL = _maybe_signed(f"{Hexadecimal.PREFIX}[\dA-Fa-f]+")
    BINARY = _maybe_signed(f"{Binary.PREFIX}[\d]+")
    OCTAL = _maybe_signed(f"{Octal.PREFIX}[0-7]+")

    return [
        HEXADECIMAL,
        BINARY,
        OCTAL,
        INTEGERS_OR_FLOATS
    ]


def _strings():
    DELIMITER = re.escape(String.DELIMITER)
    return f"{DELIMITER}[^{DELIMITER}]*{DELIMITER}"
