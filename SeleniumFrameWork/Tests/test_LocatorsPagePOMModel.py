import unittest
import pytest
import time
from SeleniumFrameWork.Pages.LocatorsPage import LocatorPage

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class EnterTextTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.et = LocatorPage(self.driver)

    @pytest.mark.run(order=4)
    def test_enterDataInEditBox(self):
        self.driver.maximize_window()
        time.sleep(2)
        self.et.enterText()
        self.et.clickOnSubmitButton()

    @pytest.mark.run(order=3)
    def test_clickOnLocatorsPage(self):
        self.et.clickOnLocatorsPage()