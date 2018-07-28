symbol = lambda tree, environment: environment.resolve(tree[1])
string = lambda tree, environment: tree[1][1:-1]
boolean = lambda tree, environment: tree[1] == "true"


# Numeric ------------------------------------------

float_ = lambda tree, environment: float(tree[1])
integer = lambda tree, environment: int(tree[1])
binary = lambda tree, environment: int(tree[1], 2)
octal = lambda tree, environment: int(tree[1], 8)
hexadecimal = lambda tree, environment: int(tree[1], 16)


# Unary Operators -----------------------------------------

def unary_positive(tree, environment):
    from limp.evaluation import evaluate
    return evaluate(tree[1], environment)


def unary_negative(tree, environment):
    from limp.evaluation import evaluate
    return -evaluate(tree[1], environment)


# Objecty Things ------------------------------------------

def list_(tree, environment):
    from limp.evaluation import evaluate
    return [evaluate(element, environment) for element in tree[1]]


def object_(tree, environment):
    from limp.evaluation import evaluate
    the_object = dict()

    pairs = tree[1]
    for key_tree, value_tree in pairs:
        key = key_tree[1]
        value = evaluate(value_tree, environment)
        the_object[key] = value
        
    return the_object


def attribute_access(tree, environment):
    from limp.evaluation import evaluate
    parent = evaluate(tree[1], environment)
    attribute = tree[2][1]
    return parent[attribute]


# Behavioural ------------------------------------------

def function_call(tree, environment):
    from limp.evaluation import evaluate
    function = evaluate(tree[1], environment)
    parameter_values = [evaluate(t, environment) for t in tree[2]]
    return function(*parameter_values)


def function(tree, environment):
    from limp.evaluation import evaluate
    parameter_names = [t[1] for t in tree[1]]

    def internal_function(*parameter_values):
        execution_environment = environment.new_child()
        parameters = zip(parameter_names, parameter_values)

        for name, value in parameters:
            execution_environment.define(name, value)

        execution_environment.define('this', internal_function)

        output = evaluate(tree[2], execution_environment)
        return output

    return internal_function


def if_statement(tree, environment):
    from limp.evaluation import evaluate
    condition = evaluate(tree[1], environment)
    if condition:
        return evaluate(tree[2], environment)
    else:
        return evaluate(tree[3], environment)
