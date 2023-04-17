import time
from SeleniumFrameWork.Base.DriverClass import WebDriverClass
import SeleniumFrameWork.Utilities.CoustomLogger as cl
from SeleniumFrameWork.Base.BasePage import BaseClass

#BasePage Part3

wd = WebDriverClass()
driver = wd.getWebDriver("chrome")

BP = BaseClass(driver)
BP.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html","Selenium Template")

Element = BP.isElementDisplayed("user_input","id")
print(Element)
BP.SendText("Code","user_input","id")



time.sleep(5)
driver.quit()