import pytest
import allure



def test_methodA():
    allureLogs("Launching App")
    allureLogs("this is Method A Step-1") # print to allure report
    print("This is method A")

def test_methodB():
    allureLogs("this is Method B Step-2")
    print("This is method B")

@pytest.mark.skip
def test_methodC():
    print("This is Method C")

def test_methodD():
    print("This is method D")
    assert False


def allureLogs(text):
    with allure.step(text):
        pass