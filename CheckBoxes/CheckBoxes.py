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

# 1. find the list of checkbox using locator
RadioButton = driver.find_elements(By.NAME,"checkbox")
time.sleep(2)

# 2. Using for loop iterate the list object and click on required option
for button in RadioButton:
    button_t =button.get_attribute("value")
    print(button_t)
    if button_t == "c3":
        button.click()
        time.sleep(5)
        print("Is Selected : ",button.is_selected())
        break


time.sleep(5)
driver.quit()

"""
    Ouptut

c1
c2
c3
Is Selected :  True

"""