import limp.internal_types.behavioural
import limp.internal_types.logical
import limp.internal_types.numeric
import limp.internal_types.standard


# Types exposed here to ease testing.
Function            = limp.internal_types.behavioural.Function
ComplexConditional  = limp.internal_types.behavioural.ComplexConditional
SimpleConditional   = limp.internal_types.behavioural.SimpleConditional
SequentialEvaluator = limp.internal_types.behavioural.SequentialEvaluator
Definition          = limp.internal_types.behavioural.Definition
Invocation          = limp.internal_types.behavioural.Invocation
Symbol              = limp.internal_types.standard.Symbol
String              = limp.internal_types.standard.String
List                = limp.internal_types.standard.List
Object              = limp.internal_types.standard.Object
Integer             = limp.internal_types.numeric.Integer
Hexadecimal         = limp.internal_types.numeric.Hexadecimal
Binary              = limp.internal_types.numeric.Binary
Octal               = limp.internal_types.numeric.Octal
Float               = limp.internal_types.numeric.Float
Boolean             = limp.internal_types.logical.Boolean


# These types are never used directly, only inherited from."
AbstractInteger     = limp.internal_types.numeric.AbstractInteger


# The order of types here is important!

# When performing type inference, the provided data will
# be checked against each type to find a valid match.

# The types will be checked in the order they
# appear in the list.
ALL_TYPES = [
    Object,
    List,
    Function,
    SimpleConditional,
    ComplexConditional,
    SequentialEvaluator,
    Definition,
    Invocation,
    Integer,
    Hexadecimal,
    Binary,
    Octal,
    Float,
    Boolean,
    String,
    Symbol
]

class Form:
    @staticmethod
    def infer_from(contents, environment):
        for type_ in ALL_TYPES:
            form = type_(contents, environment)
            if form.is_valid():
                return form
