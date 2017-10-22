def symbols():
    return {
        'chain': _chain,
        'curry': _curry,
    }


def _chain(input_, *functions):
    output = input_
    for function in functions:
        output = function(output)
    return output


def _curry(function, *early_arguments):
    return lambda *late_arguments: function(*early_arguments, *late_arguments)

