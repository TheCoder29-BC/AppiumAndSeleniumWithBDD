import time

from SeleniumFrameWork.Base.DriverClass import WebDriverClass
import SeleniumFrameWork.Utilities.CoustomLogger as cl


wd = WebDriverClass()

driver = wd.getWebDriver("chrome")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
log = cl.customLogger()
log.info("Web Page Launched")

time.sleep(5)
driver.quit()