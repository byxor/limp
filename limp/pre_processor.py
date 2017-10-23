import limp.types as Types
import limp.parentheses as Parentheses


NORMAL = 0
STRING = 1


def process(source_code):
    processed_source_code = ""
    SCAN_MODE = NORMAL
    for character in source_code:
        if SCAN_MODE == NORMAL:
            if character == Types.String.DELIMITER:
                SCAN_MODE = STRING
                processed_source_code += character
            elif character == Types.List.OPEN_DELIMITER:
                processed_source_code += f'{Parentheses.OPEN}{Types.List.KEYWORD} '
            elif character == Types.List.CLOSE_DELIMITER:
                processed_source_code += Parentheses.CLOSE
            else:
                processed_source_code += character
        elif SCAN_MODE == STRING:
            if character == Types.String.DELIMITER:
                SCAN_MODE = NORMAL
                processed_source_code += character
            else:
                processed_source_code += character
    return processed_source_code
