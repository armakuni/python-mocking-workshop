from code import cat_fact, random, random2

import pytest


# What could we mock to make this happen?
# Use unittest.mock annotations for this one: https://docs.python.org/3/library/unittest.mock.html
# Useul link: https://stackoverflow.com/questions/70184552/how-to-mock-uuid4-in-python
# Note: In our use case `src.A_script` would be `code` (the file we are trying to mock the function in)
def test_random():
    assert random() == "foo"


# How might you do this using pytest-mocks 'mocker' fixture? https://github.com/pytest-dev/pytest-mock/
# Remove the skip line to run this test
@pytest.mark.skip()
def test_random_mocker(mocker):
    assert random() == "foo"


# What could we mock to make this happen?
# Remove the skip line to run this test
@pytest.mark.skip()
def test_random2():
    assert random2() == "bar"


# How could we mock this using responses?
# An example response is:
# {
#    "fact": "A cat almost never meows at another cat, mostly just humans. Cats typically will spit, purr, and hiss at other cats.",
#    "length": 116,
# }
# Remove the skip line to run this test
@pytest.mark.skip()
def test_cat_fact():
    assert "A cat almost never meows at another cat" in cat_fact()
