import pytest

@pytest.fixture()     # декоратор, обозначающий предусловия
def before_after():
    print("Before test")
    yield
    print("\nAfter test")

def test_demo1(before_after):
    assert 1 == 1
def test_demo2(before_after):
    2 == 2