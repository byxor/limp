import limp
import limp.environment as Environment
import tests.helpers as Helpers
from nose.tools import assert_equals


object_code = '''
{
    name: "Blarg Smith"
    age: 1337
    interests: ["food" "limp" "THPS"]
    address: {
        house-number: 420
        street: "earth street"
    }
    job: "professional door knocker"
}
'''


t0 = Helpers.evaluation_fixture("test_object_literals", [
    ('{}', {}),

    ('{age: 90}', {"age": 90}),

    (object_code, {
        "name": "Blarg Smith",
        "age": 1337,
        "interests": ["food", "limp", "THPS"],
        "address": {
            "house-number": 420,
            "street": "earth street"
        },
        "job": "professional door knocker"
    }),
])


def test_accessing_attributes():
    environment = Environment.create_standard()
    environment.define('object', limp.evaluate(object_code))

    data = [
        ('{age: 90}.age',            90),
        ('{name:"Bob" age:200}.age', 200),

        ('object.name',      "Blarg Smith"),
        ('object.age',       1337),
        ('object.interests', ["food", "limp", "THPS"]),

        ('object.address', {
            "house-number": 420,
            "street": "earth street"
        }),

        ('object.address.street', "earth street"),

        ('{profiles: {byxor: {is-cool: true}}}.profiles.byxor.is-cool', True),
    ]
    
    for source_code, expected_result in data:
        result = limp.evaluate(source_code, environment)
        yield assert_equals, expected_result, result
