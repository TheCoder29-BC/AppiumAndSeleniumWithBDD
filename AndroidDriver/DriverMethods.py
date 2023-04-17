from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

#*** Step 1 : Import Appium Service class
#from appium.webdriver.appium_service import AppiumService

#*** Step 2 : create object for Appium Service Class
#lobjAppium_service = AppiumService()

#*** Step 3 : Call Start method by using Appium Service Class object
#lobjAppium_service.start()

#*** Step 4 : Create "Desired Capabilities"
desired_Caps = {}
desired_Caps['platformName'] ='Android'
desired_Caps['automationName'] = 'UiAutomator2'
desired_Caps['platformVersion'] ='10'
desired_Caps['deviceName'] = 'Pixel 3a XL'
desired_Caps['app'] = ('/Users/HW/Documents/Appium/AndroidDemoApp-main/Android_Appium_Demo.apk')
desired_Caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_Caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_Caps)

print("check if device is locked or not :", driver.is_locked())
print("Current Package :", driver.current_package)
print("Current Activity :", driver.current_activity)
print("Current Context :", driver.current_context)
print("Current orientat,on :", driver.orientation)
#output
"""
check if device is locked or not : False
Current Package : com.skill2lead.appiumdemo
Current Activity : .MainActivity
Current Context : NATIVE_APP
Current orientat,on : PORTRAIT
"""

