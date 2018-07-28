import tests.helpers as Helpers


t0 = Helpers.evaluation_fixture("test_object_literals", [
    ('{}', {}),

    ('{age: 90}', {"age": 90}),

    ('''
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
     ''',
     {
         "name": "Blarg Smith",
         "age": 1337,
         "interests": ["food", "limp", "THPS"],
         "address": {
             "house-number": 420,
             "street": "earth street"
         },
         "job": "professional door knocker"
     }
    ),

])
