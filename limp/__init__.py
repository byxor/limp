import limp.environment as Environment
import limp.errors as Errors
import limp.tokens as Tokens
import limp.token_tree as TokenTree
import limp.types as Types
import sys


def evaluate(source_code, environment=None):
    if environment is None:
        environment = Environment.create_standard()
    return Types.Form.infer_from(
        TokenTree.create_from(
            Tokens.create_from(source_code)
        ),
        environment
    ).evaluate()


class Repl:

    PROMPT = "> "

    WELCOME_MESSAGE = "Welcome to LIMP! You're in a REPL, have fun!" + "\n"

    def __init__(self, input_=input, output=sys.stdout.write):
        self._input = input_
        self._output = output
        self.__displayed_welcome = False

    def start(self):
        while True:
            self._tick()
        
    def _tick(self):
        self.__display_welcome_if_necessary()
        self.__display_prompt()
        code = self._input()
        result = self.__evaluate(code)
        self._output(f"{result}\n")

    def __display_welcome_if_necessary(self):
        if not self.__displayed_welcome:
            self._output(Repl.WELCOME_MESSAGE)
            self.__displayed_welcome = True

    def __display_prompt(self):
        self._output(Repl.PROMPT)
        sys.stdout.flush()

    def __evaluate(self, code):
        try:
            try:
                return evaluate(code)
            except Errors.EmptyCode:
                return ""
        except Exception as e:
            self.__output(f"{e}\n")
