import limp.internal_types.behavioural
import limp.internal_types.logical
import limp.internal_types.numeric
import limp.internal_types.standard
import limp.environment as Environment
from abc import ABCMeta, abstractmethod


"""
Types exposed here to ease testing.
"""
Function            = limp.internal_types.behavioural.Function
ComplexConditional  = limp.internal_types.behavioural.ComplexConditional
SimpleConditional   = limp.internal_types.behavioural.SimpleConditional
SequentialEvaluator = limp.internal_types.behavioural.SequentialEvaluator
Definition          = limp.internal_types.behavioural.Definition
Invocation          = limp.internal_types.behavioural.Invocation
Symbol              = limp.internal_types.standard.Symbol
String              = limp.internal_types.standard.String
Integer             = limp.internal_types.numeric.Integer
Hexadecimal         = limp.internal_types.numeric.Hexadecimal
Binary              = limp.internal_types.numeric.Binary
Float               = limp.internal_types.numeric.Float
Boolean             = limp.internal_types.logical.Boolean


"""
The order of types here is important!

When performing type inference, the provided data will
be checked against each type to find a valid match.

The types will be checked in the order they
appear in the list.
"""
ALL_TYPES = [
    Function,
    SimpleConditional,
    ComplexConditional,
    SequentialEvaluator,
    Definition,
    Invocation,
    Integer,
    Hexadecimal,
    Binary,
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
