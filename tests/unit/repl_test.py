import limp
import sys
import tests.helpers as Helpers
from unittest.mock import MagicMock, call
from nose.tools import *
from tests.syntax import *


ARBITRARY_NUMBER_OF_TICKS = 10
EXPECTED_OUTPUT_CALLS_PER_TICK = 2
EXPECTED_PROMPT = "> "

INPUT = 'input'
OUTPUT = 'output'
REPL = 'repl'
OUTPUT_CALL_COUNT = 'output_call_count'


def test_repl_displays_welcome_message_on_first_tick_only():
    Helpers.test_chain(
        _given_a_repl_with_mocked_streams,
        _tick,
        _output_used_at_least_once,
        _output_usage_increases_linearly_with_each_tick)


def test_repl_displays_prompt_on_every_tick():
    Helpers.test_chain(
        _given_a_repl_with_mocked_streams,
        _prompt_is_printed_on_each_tick,
        _output_used_at_least_the_number_of_ticks)

    
def test_repl_prompts_for_input_on_every_tick():
    Helpers.test_chain(
        _given_a_repl_with_mocked_streams,
        _tick_many_times,
        _input_used_once_per_tick)


def test_repl_evaluates_input_and_displays_it():
    Helpers.test_chain(
        _given_a_repl_with_mocked_streams,
        _input_is_evaluated_and_output_is_displayed([
            ("",                                          "\n"),
            (integer(10),                                 "10\n"),
            (integer(20),                                 "20\n"),
            (invoke(symbol("+"), integer(1), integer(2)), "3\n"),
        ]))


def test_repl_maintains_an_environment_across_ticks():
    variable = symbol('abc')
    Helpers.test_chain(
        _given_a_repl_with_mocked_streams,
        _next_input_is(define(variable, integer(321))),
        _tick,
        _next_input_is(variable),
        _tick,
        _output_was_written("321\n"))


### Helpers
    

def _given_a_repl_with_mocked_streams(state):
    CREATE_MOCK_STREAM = lambda: MagicMock(return_value="")
    state[INPUT] = CREATE_MOCK_STREAM()
    state[OUTPUT] = CREATE_MOCK_STREAM()
    state[REPL] = limp.Repl(state[INPUT], state[OUTPUT])
    return state


def _tick(state):
    state[REPL]._tick()
    return state


def _output_used_at_least_once(state):
    _record_output_call_count(state)
    assert_greater_equal(state[OUTPUT_CALL_COUNT], 1)
    return state


def _output_usage_increases_linearly_with_each_tick(state):
    for _ in range(ARBITRARY_NUMBER_OF_TICKS):
        _tick(state)
        expected_call_count = state[OUTPUT_CALL_COUNT] + EXPECTED_OUTPUT_CALLS_PER_TICK
        assert_equal(expected_call_count, state[OUTPUT].call_count)
        _record_output_call_count(state)
    return state


def _record_output_call_count(state):
    state[OUTPUT_CALL_COUNT] = state[OUTPUT].call_count
    return state


def _prompt_is_printed_on_each_tick(state):
    for _ in range(ARBITRARY_NUMBER_OF_TICKS):
        _tick(state)
        last_prompt_call = state[OUTPUT].mock_calls[-EXPECTED_OUTPUT_CALLS_PER_TICK]
        assert_equal(last_prompt_call, call(EXPECTED_PROMPT))
    return state


def _output_used_at_least_the_number_of_ticks(state):
    assert_greater_equal(state[OUTPUT].call_count, ARBITRARY_NUMBER_OF_TICKS)
    return state


def _tick_many_times(state):
    for _ in range(ARBITRARY_NUMBER_OF_TICKS):
        _tick(state)
    return state


def _input_used_once_per_tick(state):
    assert_equals(state[INPUT].call_count, ARBITRARY_NUMBER_OF_TICKS)
    return state


def _input_is_evaluated_and_output_is_displayed(data):
    def generated_function(state):
        for input_text, expected_output_text in data:
            _next_input_is(input_text)(state)
            _tick(state)
            _output_was_written(expected_output_text)(state)
        return state
    return generated_function


def _next_input_is(value):
    def generated_function(state):
        state[INPUT].return_value = value
        return state
    return generated_function


def _output_was_written(expected):
    def generated_function(state):
        state[OUTPUT].assert_called_with(expected)
        return state
    return generated_function
