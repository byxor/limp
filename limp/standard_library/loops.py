TIMES = "times"
ITERATE = "iterate"


def symbols():
    return {
        TIMES: _times,
        ITERATE: _iterate,
    }


def _times(iterations, callback):
    for _ in range(iterations):
        callback()


def _iterate(iterations, callback):
    for i in range(iterations):
        callback(i)
