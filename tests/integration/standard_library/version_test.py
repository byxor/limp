import tests.helpers as Helpers
import meta


def test_that_version_number_is_accessible():
    Helpers.run_evaluation_test_on([
        ("version", meta.VERSION)
    ])
