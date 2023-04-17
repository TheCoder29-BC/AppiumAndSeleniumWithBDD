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

Element = wait.until(ec.presence_of_element_located((By.ID,"user_input")))

#Element = driver.find_element(By.ID,"user_input")

ele_d = Element.is_displayed()
print("Is Displayed : ",ele_d)

ele_e = Element.is_enabled()
print("is enabled : ",ele_e)

ele_s = Element.size
print("Size of Element :" , ele_s)

ele_l = Element.location
print("Ele location : ",ele_l)

Element.click()

Element.send_keys("Code2Lead")
time.sleep(2)

Element.clear()
time.sleep(2)

Element.send_keys("Code2Lead_second time")
time.sleep(2)

ele_t = Element.get_attribute("value")
print("Text from Edit box : ",ele_t)


time.sleep(5)
driver.quit()

#to selectall ctrl+shift+alt+j or one by one alt+j

"""
    OutPut
    
Is Displayed :  True
is enabled :  True
Size of Element : {'height': 27, 'width': 171}
Ele location :  {'x': 118, 'y': 195}
Text from Edit box :  Code2Lead_second time

"""