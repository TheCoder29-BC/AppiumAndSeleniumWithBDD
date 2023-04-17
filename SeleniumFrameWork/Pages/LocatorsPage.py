import SeleniumFrameWork.Utilities.CoustomLogger as cl
from SeleniumFrameWork.Base.BasePage import BaseClass

class LocatorPage(BaseClass):

    # html Values from Locators page
    _locatorsPage = "LOCATORS"  # link
    _enterTextEditBox = "user_input"  # id
    _submitButton = "submitbutton"  # id


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def clickOnLocatorsPage(self):
        self.clickOnElement(self._locatorsPage, "link")

    def enterText(self):
        self.sendText("Code2Lead", self._enterTextEditBox, "id")
        cl.allureLogs("Entered Text in Edit Box")

    def clickOnSubmitButton(self):
        self.clickOnElement(self._submitButton, "id")
        