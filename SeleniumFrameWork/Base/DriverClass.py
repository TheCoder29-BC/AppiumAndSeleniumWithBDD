from selenium import webdriver
import SeleniumFrameWork.Utilities.CoustomLogger as cl
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self,browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            #driver = webdriver.Chrome(executable_path="/Users/sujithreddy/Documents/Code2Lead/drivers/chromedriver")
            self.log.info("Chrome Driver as initializing")
        elif browserName == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari Driver as initializing")
        elif browserName == "firefox":
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            self.log.info("Firefox Driver as initializing")
            #driver = webdriver.Firefox(executable_path="/Users/sujithreddy/Documents/Code2Lead/drivers/geckodriver")
        elif browserName == "opera":
            driver = webdriver.Opera(service=Service(OperaDriverManager().install()))
            self.log.info("Opera Driver as initializing")
        elif browserName == "edge":
            driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
            self.log.info("Edge Driver as initializing")
        return driver