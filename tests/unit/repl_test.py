import limp
import sys
from unittest.mock import MagicMock, call
from nose.tools import *


ARBITRARY_NUMBER_OF_TICKS = 10
EXPECTED_OUTPUT_CALLS_PER_TICK = 2

INPUT = None
OUTPUT = None
REPL = None


def prepare_repl():
    global INPUT
    global OUTPUT
    global REPL
    INPUT = MagicMock(return_value="")
    OUTPUT = MagicMock(return_value="")
    REPL = limp.Repl(INPUT, OUTPUT)
    

def test_repl_uses_standard_input_and_output_by_default():
    repl = limp.Repl()
    yield assert_equals, input, repl._input
    yield assert_equals, sys.stdout.write, repl._output


def test_repl_displays_welcome_message_on_first_tick():
    prepare_repl()
    REPL._tick()
    last_call_count = OUTPUT.call_count
    yield assert_greater_equal, last_call_count, 1
    for _ in range(ARBITRARY_NUMBER_OF_TICKS):
        REPL._tick()
        expected_call_count = last_call_count + EXPECTED_OUTPUT_CALLS_PER_TICK
        yield assert_equal, expected_call_count, OUTPUT.call_count
        last_call_count = OUTPUT.call_count

        
def test_repl_displays_prompt_on_every_tick():
    prepare_repl()
    EXPECTED_PROMPT = "> "
    for _ in range(ARBITRARY_NUMBER_OF_TICKS):
        REPL._tick()
        last_call = OUTPUT.mock_calls[-2]
        yield assert_equal, last_call, call(EXPECTED_PROMPT)
    yield assert_greater_equal, OUTPUT.call_count, ARBITRARY_NUMBER_OF_TICKS

    
def test_repl_prompts_for_input_on_every_tick():
    prepare_repl()
    for _ in range(ARBITRARY_NUMBER_OF_TICKS):
        REPL._tick()
    yield assert_equals, INPUT.call_count, ARBITRARY_NUMBER_OF_TICKS


def test_repl_evaluates_input_and_displays_it():
    prepare_repl()
    data = [
        ("",        "\n"),
        ("10",      "10\n"),
        ("20",      "20\n"),
        ("(+ 1 2)", "3\n"),
    ]
    for input_text, expected_output_text in data:
        INPUT.return_value = input_text
        REPL._tick()
        yield OUTPUT.assert_called_with, expected_output_text


def test_repl_maintains_an_environment_across_ticks():
    prepare_repl()
    INPUT.return_value = '(define abc 321)'
    REPL._tick()
    INPUT.return_value = 'abc'
    REPL._tick()
    yield OUTPUT.assert_called_with, "321\n"
