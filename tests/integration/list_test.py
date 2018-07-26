import tests.helpers as Helpers
from tests.syntax import *


t0 = Helpers.evaluation_fixture("test", [
    (list_of(integer(1), integer(2), integer(3)), [1, 2, 3]),
    (list_of(string("celery"), string("man")),    ["celery", "man"]),
])
