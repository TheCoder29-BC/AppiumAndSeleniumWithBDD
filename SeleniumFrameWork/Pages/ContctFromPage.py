import SeleniumFrameWork.Utilities.CoustomLogger as cl
from SeleniumFrameWork.Base.BasePage import BaseClass


class ContactFrom(BaseClass):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators Values in Contact form Page
    _contactFromPage = "FORM"  # link
    _formPage = "reused_form"  # id
    _enterName = "name"  # id
    _enterEmail = "emai"  # id
    _enterMessage = "message"  # id
    _getCaptcha = "captcha_image"  # id
    _enterCaptha = "captcha"  # id
    _postButton = "btnContactUs"  # id

    def ClickContact(self):
        self.ClickOnElement(self._contactFromPage,"link")
        cl.allureLogs("Clicked on Contact Form")

    def verifyFormPage(self):
        element = self.isElementDisplayed(self._formPage, "id")
        assert element == True
        cl.allureLogs("Clicked on Contact Form")

    def enterName(self):
        self.sendText("Code2Lead", self._enterName, "id")
        cl.allureLogs("Clicked on Contact Form")

    def enterEmail(self):
        self.SendText("abc@gmail.com", self._enterEmail, "id")
        cl.allureLogs("Clicked on Contact Form")

    def enterMessage(self):
        self.SendText("This is a Code2Lead", self._enterMessage, "id")
        cl.allureLogs("Clicked on Contact Form")

    def getCaptha(self):
        cap = self.getText(self._getCaptcha, "id")
        cl.allureLogs("Clicked on Contact Form")
        return cap

    def enterCaptha(self):
        self.SendText(self.getCaptha(), self._enterCaptha, "id")
        cl.allureLogs("Clicked on Contact Form")

    def clickOnPostButton(self):
        self.scrollTo(self._postButton, "id")
        self.clickOnElement(self._postButton, "id")
        cl.allureLogs("Clicked on Contact Form")
        