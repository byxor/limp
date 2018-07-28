import limp.syntax_tree as SyntaxTree
import limp.evaluators as Evaluators


def evaluate(tree, environment):
    type_ = tree[0]
    evaluator = _evaluators[type_]
    return evaluator(tree, environment)


_TreeTypes = SyntaxTree.Types


_evaluators = {
    _TreeTypes.Symbol: Evaluators.symbol,

    _TreeTypes.Float:       Evaluators.float_,
    _TreeTypes.Integer:     Evaluators.integer,
    _TreeTypes.Binary:      Evaluators.binary,
    _TreeTypes.Octal:       Evaluators.octal,
    _TreeTypes.Hexadecimal: Evaluators.hexadecimal,

    _TreeTypes.String:  Evaluators.string,
    _TreeTypes.Boolean: Evaluators.boolean,
    _TreeTypes.List:    Evaluators.list_,

    _TreeTypes.Object:          Evaluators.object_,
    _TreeTypes.AttributeAccess: Evaluators.attribute_access,

    _TreeTypes.UnaryNegative: Evaluators.unary_negative,
    _TreeTypes.UnaryPositive: Evaluators.unary_positive,

    _TreeTypes.Function:     Evaluators.function,
    _TreeTypes.FunctionCall: Evaluators.function_call,
    _TreeTypes.IfStatement:  Evaluators.if_statement,
}

