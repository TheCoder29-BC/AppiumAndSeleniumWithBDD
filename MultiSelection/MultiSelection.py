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
ele = wait.until(ec.presence_of_element_located((By.ID,"multiselect")))

# import the Select class
from selenium.webdriver.support.select import Select

# Create the object for Select class
multiSelect_opt = Select(ele)
print("Check whether it is a multi select or not : ",multiSelect_opt.is_multiple) #is not gives Fales
# list the values
multiSelect_val =  multiSelect_opt.options
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

#Select again
# click by Index
multiSelect_opt.select_by_index(2)

# click by Value
multiSelect_opt.select_by_value("mOptionOne")

# Click by Text
multiSelect_opt.select_by_visible_text("mOption3")

time.sleep(2)


time.sleep(5)
driver.quit()

"""
    Output 
    
Check whether it is a multi select or not :  True
mOptions
mOption1
mOption2
mOption3
mOption4
mOption5
"""