# Contributing to LIMP

Hi there, I'm thrilled that you want to contribute to this project!

Here are some requirements that must be met before your feature is eligible for merging:


## 1. Your code must be tested (via fully-automated tests).

This is often frustrating for some developers, but I can't stress enough how crucial it is.

**Why should I test my feature?**
* You'll be confident that it works.
* You won't have to spend time manually checking things over and over.
* You can refactor your feature safely without worrying about breaking it (just re-run the tests).
* Everyone else will know when they change something that breaks your feature, preventing a lot of bugs from sneaking in.
* The tests will enable us to restructure the code without fear of breakage.

**How can I test my feature?**

_tests/unit/string_reversal_test.py_
```python
from limp.utils import reverse
from nose.tools import assert_equal


def test():
    data = [
        ("",                   ""),
        ("a",                  "a"),
        ("car",                "rac"),
        ("Reverse!",           "!esreveR"),
        ("racecar",            "racecar"),
        ("hello there fellas", "sallef ereht olleh"),
    ]
    for input_, expected_output in data:
        actual_output = reverse(input_)
        yield assert_equal, expected_output, actual_output
```

_limp/utils.py_
```python
def reverse(string):
    return string[::-1]
```

* A common pattern in our tests involves constructing tuples of inputs and expected outputs. This helps to reduce the complexity of tests and reduce duplicated function calls. It also encourages purer functions.

* It often works well to name your test file like a _feature_. By doing this, you're implicitly breaking structural coupling between the tests and the feature under test.

* Make sure the file ends in `test.py` so the test runner picks it up. The functions usually also need to have `test` in them.

* If the test's file name succintly describes the feature, call your test function `test` to reduce repetition.

---

If you're unsure of what tests to write, take a look at some of the existing ones.

If you're unsure on the difference between unit and integration tests, research the differences.

If you want motivation to write tests, watch almost _any_ Uncle Bob video on YouTube.


## 2. Your code must meet certain style requirements.

Currently there isn't a definitive style guide being followed. This will hopefully change in the future.


#### Common style requirements:

* Use 4 spaces for indentation.
* Use 2 blank new-lines between every independent concept in a module.
* Use `snake_case` for functions, methods, and variables.
* Use `PascalCase` for classes.
* Define constants in `SCREAMING_SNAKE_CASE`.
* Prefix "private" functions in modules with 1 leading underscore.
* Prefix "private" functions in classes with 2 leading underscores.


#### Niche style requirements:

* Import limp modules like this: `import limp.pre_processor as PreProcessor`
* Avoid writing the project name throughout the code; the project name may change some day.
* Avoid duplicating words/concepts between module and function names.  
(`limp.tokens.create_from` :white_check_mark:, `limp.tokens.create_tokens_from` :x:)
* When writing tabular/tuple/list-based tests, try to line up the expected output on the same column. See [this test](https://github.com/byxor/limp/blob/master/tests/integration/standard_library/boolean_test.py) for an example.

If your code is [PEP8](https://www.python.org/dev/peps/pep-0008/) Compliant, it will be A-okay. :ok_hand:

## 3. Your code does not impose restrictions on structure/architecture/implementation.

This is extremely hard to measure, but try to leave the code as malleable as possible for future developers. The easiest way to do this is through automated tests.

If you have a function to perform some kind of task, try not to expose what's going on internally. This allows other people to change the implementation without affecting behaviour from the outside. For example, call a function `define_symbol` instead of `add_symbol_to_dictionary`, and don't add getters/setters to classes if they perform behaviour.

#### An example of code that encourages flexibility:

Notice how none of the integration tests explicitly have any LIMP code in them. This choice was made so that the language syntax could be freely changed. If the tests were full of statically-written LIMP code, the tests would restrict change.

If we weren't doing this, and we wanted to change addition from `+` to `add`, all the tests that expected the `+` symbol to exist would break.

The integration tests allow us to be flexible because they are [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).
