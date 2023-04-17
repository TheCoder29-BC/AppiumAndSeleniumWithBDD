"""
ExplicitWait:
ExplicitWait is defined as maximum time to wait for a given condition before throws an error.

Example :
If you declare ExplicitWait with a condition presence_of_element_located and time 25 seconds ,
if WebElement is visible less than 25 seconds then it will click or do the respective operation on that particular WebElement.
or it will wait for max 25 sec before in throws an error or exception

#list of Selenium Exceptions
#https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html

"""
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.dummypoint.com/seleniumtemplate.html") #Uses to launch the webpage

time.sleep(5)

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
ele = wait.until(ec.presence_of_element_located((By.ID,"user_input")))
ele.send_keys("Code2Lead")

time.sleep(5)
driver.quit()