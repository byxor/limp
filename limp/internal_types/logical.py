import limp.internal_types.form as Form


class Boolean(Form.Constructor):

    TRUE_KEYWORD = 'true'
    FALSE_KEYWORD = 'false'

    VALUES = {
        TRUE_KEYWORD: True,
        FALSE_KEYWORD: False
    }

    def evaluate(self):
        return Boolean.VALUES[self._contents]

    def is_valid(self):
        return self._contents in Boolean.VALUES
