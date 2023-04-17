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
ele = wait.until(ec.presence_of_element_located((By.ID,"dropdown")))

# import the Select class
from selenium.webdriver.support.select import Select

# Create the object for Select class
dropdown_Opt = Select(ele)
# List the values in Drop Down
dd_v = dropdown_Opt.options
for DropDown_Value in dd_v:
    print(DropDown_Value.text)

# Click by Index
dropdown_Opt.select_by_index(2)
time.sleep(2)
# Click by Value
dropdown_Opt.select_by_value("OptionThree")
time.sleep(2)
#Click by Text
dropdown_Opt.select_by_visible_text("Option5")
time.sleep(5)


time.sleep(5)
driver.quit()

"""
    Output

Options
Option1
Option2
Option3
Option4
Option5

"""