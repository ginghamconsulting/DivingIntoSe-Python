import pytest

@pytest.fixture
def base_test(selenium):
    return selenium