import tests.helpers as Helpers
import meta


t0 = Helpers.evaluation_fixture("test_that_version_number_is_accessible", [
    ("version", meta.VERSION)
])

