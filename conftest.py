import pytest


@pytest.fixture
def mock_cat_fact_response():
    return {
        "fact": "A cat almost never meows at another cat, mostly just humans. Cats typically will spit, purr, and hiss at other cats.",
        "length": 116,
    }
