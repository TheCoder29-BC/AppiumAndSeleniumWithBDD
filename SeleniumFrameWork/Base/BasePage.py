from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from traceback import print_stack
import SeleniumFrameWork.Utilities.CoustomLogger as cl
from selenium.webdriver.support.select import Select

import allure

class BaseClass:
    log = cl.customLogger()

    def __init__(self,driver):
        self.driver = driver

    def launchWebPage(self,url,title):
        try:
            self.driver.get(url)
            assert  title in self.driver.title
            self.log.info("Web Page Launched with URL : "+ url)

        except:
            self.log.info("Web Page cannot be Launched with URL : "+ url)


    #part 2
    def getLocatorType(self,LocatorType):
        LocatorType = LocatorType.lower()
        if LocatorType == "id":
            return By.ID
        elif LocatorType == "name":
            return By.NAME
        elif LocatorType == "class":
            return By.CLASS_NAME
        elif LocatorType == "xpath":
            return By.XPATH
        elif LocatorType == "css":
            return By.CSS_SELECTOR
        elif LocatorType == "tag":
            return By.TAG_NAME
        elif LocatorType == "link":
            return By.LINK_TEXT
        elif LocatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator Type : " + LocatorType + " entered is not found")
        return False

    def getWebElement(self,LocatorValue,LocatorType="id"):
        webElement = None
        try:
            LocatorType = LocatorType.lower()
            locatorByType = self.getLocatorType(LocatorType)
            webElement = self.driver.find_element(locatorByType, LocatorValue)
            self.log.info("WebElement found with locator value " + LocatorValue + " using LocatorType " + locatorByType)
        except:
            self.log.error(
                "WebElement not found with locator value " + LocatorValue + " using LocatorType " + LocatorType)
        return webElement

    #Part 3
    def waitForElement(self,LocatorValue,LocatorType="id"):
        WebElement = None
        try:
            LocatorType = LocatorType.lower()
            locatorByType = self.getLocatorType(LocatorType)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            WebElement = wait.until(ec.presence_of_element_located((locatorByType, LocatorValue)))
            self.log.info("WebElement found with locator value " + LocatorValue + " using LocatorType " + LocatorType)
        except:
            self.log.error("WebElement not found with locator value " + LocatorValue + " using LocatorType " + LocatorType)
        return WebElement

    def ClickOnElement(self,LocatorValue,LocatorType="id"):
        try:
            LocatorType = LocatorType.lower()
            WebElement = self.waitForElement(LocatorValue,LocatorType)
            WebElement.click()
            self.log.info(
                "Clicked on WebElement with locator value " + LocatorValue + " using LocatorType " + LocatorType)
        except:
            self.log.error(
                "Unable to Click on WebElement with locator value " + LocatorValue + " using LocatorType " + LocatorType)

    def SendText(self,text,LocatorValue,LocatorType="id"):
        try:
            LocatorType = LocatorType.lower()
            WebElement = self.waitForElement(LocatorValue, LocatorType)
            WebElement.send_keys(text)
            self.log.info("Sent the text " + text + " in WebElement with locator value " + LocatorValue + " using LocatorType " + LocatorType)
        except:
            self.log.error("Unable to Sent the text " + text + " in WebElement with locator value " + LocatorValue + "using LocatorType " + LocatorType)
            self.takeScreenshot(LocatorType)

    #Part 4
    def getText(self, LocatorValue, LocatorType="id"):
        elementText = None
        try:
            LocatorType = LocatorType.lower()
            webElement = self.waitForElement(LocatorValue, LocatorType)
            elementText = webElement.text
            self.log.info(
                "Got the text " + elementText + " from WebElement with locator value " + LocatorValue + " using LocatorType " + LocatorType)
        except:
            self.log.error(
                "Unable to get the text " + elementText + " from WebElement with locator value " + LocatorValue + "using LocatorType " + LocatorType)
            print_stack()

        return elementText

    def isElementDisplayed(self, LocatorValue, LocatorType="id"):
        elementDisplayed = None
        try:
            LocatorType = LocatorType.lower()
            webElement = self.waitForElement(LocatorValue, LocatorType)
            elementDisplayed = webElement.is_displayed()
            self.log.info(
                "WebElement is Displayed on web page with locator value " + LocatorValue + " using LocatorType " + LocatorType)
        except:
            self.log.error(
                "WebElement is not Displayed on web page with locator value " + LocatorValue + " using LocatorType " + LocatorType)
            print_stack()

        return elementDisplayed

    def scrollTo(self, LocatorValue, LocatorType="id"):
        actions = ActionChains(self.driver)
        try:
            LocatorType = LocatorType.lower()
            webElement = self.waitForElement(LocatorValue, LocatorType)
            actions.move_to_element(webElement).perform()
            self.log.info(
                "Scrolled to WebElement with locator value " + LocatorValue + " using LocatorType " + LocatorType)
        except:
            self.log.error(
                "Unable to scroll to WebElement with locator value " + LocatorValue + "using LocatorType " + LocatorType)
            print_stack()

    #Final Part
    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def ClickOnRadioButton(self,RadioBtValue,LocatorValue,LocatorType="id"):
        try:
            LocatorType = LocatorType.lower()
            WebElement = self.waitForElement(LocatorValue, LocatorType)
            # 2. Using for loop iterate the list object and click on required option
            for button in WebElement:
                button_t = button.get_attribute("value")
                if button_t == RadioBtValue:
                    button.click()
                    time.sleep(5)
                    self.log.error("able to click on RadioButton with locator value " + LocatorValue + "using LocatorType " + LocatorType + "in :"+RadioBtValue)
                    break
        except:
            self.log.error("Unable to click on RadioButton with locator value " + LocatorValue + "using LocatorType " + LocatorType + "in :"+RadioBtValue)
            print_stack()

    def ClickOnComboBox(self):
        try:
            LocatorType = LocatorType.lower()
            WebElement = self.waitForElement(LocatorValue, LocatorType)
            # 2. Using for loop iterate the list object and click on required option
            for button in WebElement:
                button_t = button.get_attribute("value")
                if button_t == RadioBtValue:
                    button.click()
                    time.sleep(5)
                    self.log.error("able to click on RadioButton with locator value " + LocatorValue + "using LocatorType " + LocatorType + "in :"+RadioBtValue)
                    break
        except:
            self.log.error("Unable to click on RadioButton with locator value " + LocatorValue + "using LocatorType " + LocatorType + "in :"+RadioBtValue)
            print_stack()

#under Devolepment
"""
    class MultiSelection:
        log = cl.customLogger()

        def __init__(self, driver):
            self.driver = driver

        def getLocatorType(self, LocatorType):
            LocatorType = LocatorType.lower()
            if LocatorType == "id":
                return By.ID
            elif LocatorType == "name":
                return By.NAME
            elif LocatorType == "class":
                return By.CLASS_NAME
            elif LocatorType == "xpath":
                return By.XPATH
            elif LocatorType == "css":
                return By.CSS_SELECTOR
            elif LocatorType == "tag":
                return By.TAG_NAME
            elif LocatorType == "link":
                return By.LINK_TEXT
            elif LocatorType == "plink":
                return By.PARTIAL_LINK_TEXT
            else:
                self.log.error("Locator Type : " + LocatorType + " entered is not found")
            return False

        def waitForElement(self, LocatorValue, LocatorType="id"):
            WebElement = None
            try:
                LocatorType = LocatorType.lower()
                locatorByType = self.getLocatorType(LocatorType)
                wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                     ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
                WebElement = wait.until(ec.presence_of_element_located((locatorByType, LocatorValue)))
                self.log.info(
                    "WebElement found with locator value " + LocatorValue + " using LocatorType " + LocatorType)
            except:
                self.log.error(
                    "WebElement not found with locator value " + LocatorValue + " using LocatorType " + LocatorType)
            return WebElement

        def MultiSelection(self):
            wait = WebDriverWait(driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            ele = wait.until(ec.presence_of_element_located((By.ID, "multiselect")))
            # Create the object for Select class
            multiSelect_opt = Select(ele)
            print("Check whether it is a multi select or not : ", multiSelect_opt.is_multiple)  # is not gives Fales
            # list the values
            multiSelect_val = multiSelect_opt.options
            for multiSelect_values in multiSelect_val:
                print(multiSelect_values.text)
            # click by Index
            multiSelect_opt.select_by_index(2)
            # click by Value
            multiSelect_opt.select_by_value("mOptionOne")
            # Click by Text
            multiSelect_opt.select_by_visible_text("mOption3")
            time.sleep(2)
            # deselect_by_index
            multiSelect_opt.deselect_by_index(2)
            # deselect_by_value
            multiSelect_opt.deselect_by_value("mOptionOne")
            # deselect_by_visible_text
            multiSelect_opt.deselect_by_visible_text("mOption3")
            # deselect_all
            multiSelect_opt.deselect_all()
            # Select again
            # click by Index
            multiSelect_opt.select_by_index(2)
            # click by Value
            multiSelect_opt.select_by_value("mOptionOne")
            # Click by Text
            multiSelect_opt.select_by_visible_text("mOption3")
        
"""""