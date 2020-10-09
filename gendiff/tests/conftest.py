import pytest


@pytest.fixture()
def case_data():
    print("\nTest Start")
    yield open('gendiff/tests/fixtures/result.txt', 'r')
    print("\nEnd of test")