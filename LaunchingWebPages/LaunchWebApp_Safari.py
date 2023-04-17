#to run in Safari go to settings -> Advanced -> dialogbox Show develop menu in menu bar ACTIVE
#click on Develop on Menu bar then Mark the Allow Remote Automation

from selenium import webdriver
import time

driver = webdriver.Safari()

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

time.sleep(5)
driver.quit()