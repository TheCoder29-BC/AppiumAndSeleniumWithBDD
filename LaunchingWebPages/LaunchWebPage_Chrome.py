#First check the Chrome Version ---->chrome://settings/help
#then download the chromedriver
import time

#take the chromedriver path
#C:\Users\HW\Documents\Appium\AndroidDemoApp-main\ChromeDriver\chromedriver.exe

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/HW/Documents/Appium/AndroidDemoApp-main/ChromeDriver/chromedriver.exe")

driver.get("http://www.dummypoint.com/seleniumtemplate.html") #Uses to launch the webpage

time.sleep(5)

driver.quit()
#If you get DeprecationWarning: executable_path has been deprecated, please pass in a Service object
#driver = webdriver.Chrome("C:/Users/HW/Documents/Appium/AndroidDemoApp-main/ChromeDriver/chromedriver.exe")
#Solution
 #https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python