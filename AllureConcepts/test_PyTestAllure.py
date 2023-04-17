import pytest
import allure



def test_methodA():
    print("This is method A")

def test_methodB():
    print("This is method B")

@pytest.mark.skip
def test_methodC():
    print("This is Method C")

def test_methodD():
    print("This is method D")
    assert False


