import limp.internal_types.form as Form


class Boolean(Form.Constructor):

    TRUE_KEYWORD = 'true'
    FALSE_KEYWORD = 'false'

    MAP = {
        TRUE_KEYWORD: True,
        FALSE_KEYWORD: False
    }

    def evaluate(self):
        return Boolean.MAP[self._contents]

    def is_valid(self):
        return self._contents in Boolean.MAP
