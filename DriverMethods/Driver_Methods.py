from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.dummypoint.com/seleniumtemplate.html") #Uses to launch the webpage

assert "Selenium Template" in driver.title

driver.maximize_window()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.maximize_window()

time.sleep(5)
driver.quit()

