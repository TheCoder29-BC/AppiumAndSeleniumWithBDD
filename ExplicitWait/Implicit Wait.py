"""
An implicit wait tells WebDriver to polll the DOM for a certain amount of time when trying to
find any element (or elements) not immediately available
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.dummypoint.com/seleniumtemplate.html") #Uses to launch the webpage

time.sleep(5)

driver.implicitly_wait(10)#it will wait 10seconds
#it will then walk on the partical element.

driver.find_element(By.ID,"user_input").send_keys("Test2Test3Test")