import time
from SeleniumFrameWork.Base.DriverClass import WebDriverClass
import SeleniumFrameWork.Utilities.CoustomLogger as cl
from SeleniumFrameWork.Base.BasePage import BaseClass
from SeleniumFrameWork.Pages.ContctFromPage import ContactFrom

#ContactFormPage Design using POM Model

wd = WebDriverClass()
driver = wd.getWebDriver("chrome")

BP = BaseClass(driver)
CF = ContactFrom(driver)

BP.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html","Selenium Template")
CF.ClickContact()
time.sleep(5)
CF.verifyFormPage()
CF.enterName()
CF.enterEmail()
CF.enterEmail()
CF.enterMessage()
CF.enterCaptha()
CF.clickOnPostButton()



time.sleep(5)
driver.quit()