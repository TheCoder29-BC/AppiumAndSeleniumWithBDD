import time
from SeleniumFrameWork.Base.DriverClass import WebDriverClass
import SeleniumFrameWork.Utilities.CoustomLogger as cl
from SeleniumFrameWork.Base.BasePage import BaseClass

#BasePage Part3

wd = WebDriverClass()
driver = wd.getWebDriver("chrome")

BP = BaseClass(driver)
BP.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html","Selenium Template")


#BP.SendText("Code","user_input","id")

BP.ClickOnElement("Form","link")

time.sleep(5)
driver.quit()