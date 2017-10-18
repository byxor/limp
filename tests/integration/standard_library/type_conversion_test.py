import tests.helpers as Helpers


def test():
    Helpers.run_evaluation_test_on([
        ('(string 123)', "123"),
        ('(string 999)', "999"),
        ('(string 0)',   "0"),

        ('(integer "32")', 32),
        ('(integer "-1")', -1),

        ('(float "4.2")',  4.2),
        ('(float "97.4")', 97.4),

        ('(boolean "false")', False),
        ('(boolean "true")',  True),
    ])
