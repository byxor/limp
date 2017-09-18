import limp.parentheses as Parentheses
import limp.types as Types
from collections import namedtuple


def create_from(source_code):
    source_code = _pad_characters(source_code, Parentheses.ALL)
    SCAN_MODES = {
        'NORMAL': _scan_in_normal_mode, 
        'STRING': _scan_in_string_mode,
    }
    algorithm_step = _AlgorithmStep(token='', ready_to_append=True, next_mode='NORMAL')
    tokens = []    
    for character in source_code:
        scan_function = SCAN_MODES[algorithm_step.next_mode]
        algorithm_step = scan_function(character, algorithm_step.token)
        algorithm_step = _append_token_if_ready(algorithm_step, tokens)
        mode = algorithm_step.next_mode
    algorithm_step = _AlgorithmStep(algorithm_step.token, True, algorithm_step.next_mode)
    _append_token_if_ready(algorithm_step, tokens)
    return tokens


def _pad_characters(source_code, characters):
    if characters == []:
        return source_code
    return _pad_characters(_pad(source_code, characters[0]), characters[1:])


def _pad(source_code, character):
    return source_code.replace(character, ' {} '.format(character))


def _scan_in_string_mode(character, current_token):
    current_token += character
    ready_to_append = False
    next_mode = 'STRING'
    if character == Types.String.DELIMITER:
        ready_to_append = True
        next_mode = 'NORMAL'
    return _AlgorithmStep(current_token, ready_to_append, next_mode)


def _scan_in_normal_mode(character, current_token):
    ready_to_append = False
    next_mode = 'NORMAL'
    if character.isspace():
        ready_to_append = True
    else:
        current_token += character
        if character == Types.String.DELIMITER:
            next_mode = 'STRING'
    return _AlgorithmStep(current_token, ready_to_append, next_mode)


def _append_token_if_ready(algorithm_step, tokens):
    if algorithm_step.ready_to_append:
        if not _empty(algorithm_step.token):
            tokens.append(algorithm_step.token)
            return _AlgorithmStep('', False, algorithm_step.next_mode)
    return algorithm_step

        
def _empty(string):
    return string == ""


_AlgorithmStep = namedtuple('_AlgorithmStep', 'token ready_to_append next_mode')
