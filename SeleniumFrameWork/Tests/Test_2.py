import time
from SeleniumFrameWork.Base.DriverClass import WebDriverClass
import SeleniumFrameWork.Utilities.CoustomLogger as cl
from SeleniumFrameWork.Base.BasePage import BaseClass

#with first BasePage class

wd = WebDriverClass()

driver = wd.getWebDriver("chrome")
bp = BaseClass(driver)
bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html","Selenium Template")

log = cl.customLogger()
log.info("Web Page Launched")

time.sleep(5)
driver.quit()