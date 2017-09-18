import limp.environment as Environment
import limp.tokens as Tokens
import limp.token_tree as TokenTree
import limp.types as Types


def evaluate(source_code, environment=None):
    if environment is None:
        environment = Environment.create_standard()
    return Types.Form.infer_from(
        TokenTree.create_from(
            Tokens.create_from(source_code)
        ),
        environment
    ).evaluate()
