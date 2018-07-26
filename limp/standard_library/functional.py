PARTIAL = "partial"
CHAIN = "chain"


def symbols():
    return {
        PARTIAL: _partial,
        CHAIN: _chain,
    }


def _chain(input_, *functions):
    output = input_
    for function in functions:
        output = function(output)
    return output


def _partial(function, *early_arguments):
    return lambda *late_arguments: function(*early_arguments, *late_arguments)
