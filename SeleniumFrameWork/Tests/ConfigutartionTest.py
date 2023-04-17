import pytest
from SeleniumFrameWork.Base.BasePage import BaseClass
from SeleniumFrameWork.Base.DriverClass import WebDriverClass
import time


@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("chrome")
    BP = BaseClass(driver)
    BP.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html","Selenium Template")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')


@pytest.yield_fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
