from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.dummypoint.com/seleniumtemplate.html") #Uses to launch the webpage

time.sleep(5)

#to find all elements

ele = driver.find_elements(By.CLASS_NAME,"section-header") #multiple Elements
print(ele) #output [<selenium.webdriver.remote.webelement.WebElement (session="ac59dba9bc96920f7e7dc9b844176aa4", element="c9ce46be-cf66-403a-bf01-bae4d3ef0bf0")>]


for menu in ele:
    print(menu.text)
#output
"""
Locators
Form
DragAndDrop
Frame
Windows
Actions
Tables
"""
time.sleep(5)
driver.quit()