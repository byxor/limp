import limp.environments as Environments
import limp.evaluation as Evaluation
import limp.syntax_tree as SyntaxTree
import limp.tokens as Tokens


def evaluate(source_code):
    return Evaluation.execute(
        SyntaxTree.create_from(
            Tokens.create_from(
                source_code)),
        Environments.create_standard()
    )
