import limp.errors as Errors
import limp.parentheses as Parentheses
import limp.types as Types
from limp.utils import is_empty
from collections import namedtuple
from enum import Enum


def create_from(source_code):
    if is_empty(source_code.strip()):
        raise Errors.EmptyCode()
    source_code = _pad_parentheses(source_code)
    algorithm_step = _AlgorithmStep(token='', ready_to_append=True, next_mode=_ScanMode.NORMAL)
    tokens = []
    for character in source_code:
        scan_mode = algorithm_step.next_mode
        algorithm_step = scan_mode(character, algorithm_step.token)
        algorithm_step = _append_token_if_ready(algorithm_step, tokens)
    algorithm_step = _AlgorithmStep(algorithm_step.token, True, algorithm_step.next_mode)
    _append_token_if_ready(algorithm_step, tokens)
    _assert_structure_is_valid(tokens)
    return tokens


# Padding the parentheses with spaces
# makes the source_code easier to
# extract tokens from.
def _pad_parentheses(source_code):
    def pad(x): return f' {x} '
    padded_source_code = ''
    scanning_string = False
    for character in source_code:
        chunk = character
        if not scanning_string:
            if character == Types.String.DELIMITER:
                scanning_string = True
            elif character in Parentheses.ALL:
                chunk = pad(character)
        else:
            if character == Types.String.DELIMITER:
                scanning_string = False
        padded_source_code += chunk
    return padded_source_code


_AlgorithmStep = namedtuple('_AlgorithmStep', 'token ready_to_append next_mode')


def _scan_in_normal_mode(character, current_token):
    ready_to_append = False
    next_mode = _ScanMode.NORMAL
    if character.isspace():
        ready_to_append = True
    else:
        current_token += character
        if character == Types.String.DELIMITER:
            next_mode = _ScanMode.STRING
    return _AlgorithmStep(current_token, ready_to_append, next_mode)


def _scan_in_string_mode(character, current_token):
    current_token += character
    ready_to_append = False
    next_mode = _ScanMode.STRING
    if character == Types.String.DELIMITER:
        ready_to_append = True
        next_mode = _ScanMode.NORMAL
    return _AlgorithmStep(current_token, ready_to_append, next_mode)


class _ScanMode(Enum):
    NORMAL = _scan_in_normal_mode
    STRING = _scan_in_string_mode


def _append_token_if_ready(algorithm_step, tokens):
    if algorithm_step.ready_to_append:
        if not is_empty(algorithm_step.token):
            tokens.append(algorithm_step.token)
            return _AlgorithmStep('', False, algorithm_step.next_mode)
    return algorithm_step


def _assert_structure_is_valid(tokens):
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
