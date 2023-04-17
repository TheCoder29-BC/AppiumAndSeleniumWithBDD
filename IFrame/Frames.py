from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException,ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.common.alert import Alert

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.dummypoint.com/Frame.html") #Uses to launch the webpage

time.sleep(5)

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

Element_Frame = driver.find_elements(By.TAG_NAME, "iframe")

# To display number of IFrames in web page
print("List of iframe : ",len(Element_Frame))

""" ---Example 1 ---
# Switch to IFrame by Index
time.sleep(2)
driver.switch_to.frame(1)

Data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",Data.text)
-----------------------------------
-----------Output-----------------
List of iframe :  4
Frame Name is :  Frame 2
"""

""" --- Example 2 ---
# Switch to IFrame by Name
time.sleep(2)
driver.switch_to.frame("framename") #is th <iframe name='...'..>

Data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",Data.text)

"""

""" --- Example 3 ---
# Switch to IFrame by ID
time.sleep(2)
driver.switch_to.frame("f3")

Data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",Data.text)

"""

# Switch to IFrame by WebElement
time.sleep(2)
Element_Frame = driver.find_element(By.ID,"f2")
driver.switch_to.frame(Element_Frame)

DaTa = driver.find_element(By.ID,"framename")
print("Frame Name is : ",DaTa.text)

# Switching back to normal content page from frame
time.sleep(2)
driver.switch_to.default_content()

DaTa = driver.find_element(By.ID,"framename")
print("Webpage Name is : ",DaTa.text)

time.sleep(5)
driver.quit()