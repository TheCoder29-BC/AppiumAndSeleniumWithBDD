from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application") #using chromedriver

Driver.get("http://www.dummypoint.com/seleniumtemplate.html")
assert "Selenium Template" in Driver.title

time.sleep(2)
Driver.find_element(By.ID,"user inpu".send_keys("code"))

time.sleep(2)
Driver.quit()