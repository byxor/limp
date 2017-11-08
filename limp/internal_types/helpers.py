from functional import seq


def evaluate(node, environment):
    return _evaluated(_to_form(node, environment))


def evaluate_list_of(nodes, environment):
    _to_form_ = lambda node: _to_form(node, environment)
    return list(seq(nodes)
            .map(_to_form_)
            .map(_evaluated))


def _to_form(node, environment):
    from limp.types import Form
    return Form.infer_from(node, environment)


def _evaluated(form):
    return form.evaluate()
