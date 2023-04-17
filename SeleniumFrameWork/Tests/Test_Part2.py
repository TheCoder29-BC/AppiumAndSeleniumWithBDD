import time
from SeleniumFrameWork.Base.DriverClass import WebDriverClass
import SeleniumFrameWork.Utilities.CoustomLogger as cl
from SeleniumFrameWork.Base.BasePage import BaseClass

#BasePage Part2

wd = WebDriverClass()

driver = wd.getWebDriver("chrome")
bp = BaseClass(driver)
bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html","Selenium Template")

log = cl.customLogger()
log.info("Web Page Launched")

WebElement = bp.getWebElement("user_input","id")
WebElement.send_keys("Code2Code")

time.sleep(5)
driver.quit()