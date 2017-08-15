import limp.environment as Environment
import limp.evaluation as Evaluation
import limp.syntax_tree as SyntaxTree
import limp.tokens as Tokens


def evaluate(source_code, environment=None):
    if environment is None:
        environment = Environment.create_standard()
    return Evaluation.execute(
        SyntaxTree.create_from(
            Tokens.create_from(
                source_code)),
        environment
    )
