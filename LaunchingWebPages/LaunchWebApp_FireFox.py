#first you need to download geckodriver for firefox
#https://github.com/mozilla/geckodriver/releases


from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="C:/Users/HW/Documents/Appium/AndroidDemoApp-main/GeckoDriver(Firefox)/geckodriver.exe")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

time.sleep(5)
driver.quit()