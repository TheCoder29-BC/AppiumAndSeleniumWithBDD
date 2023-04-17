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

lobjElement_id = driver.find_element(AppiumBy.ID,"com.skill2lead.appiumdemo:id/EnterValue")
lobjElement_id.click()

time.sleep(3)

lobjElement_class = driver.find_element(AppiumBy.CLASS_NAME,'android.widget.EditText')
lobjElement_class.send_keys("Test2Test")

#Key_Code
#https://developer.android.com/reference/android/view/KeyEvent.html#KEYCODE_ENTER
lobjElement_class.click()
driver.press_keycode(67) #press the clear button
driver.press_keycode(67) #press the clear button

time.sleep(2)

driver.press_keycode(4) #back key
driver.press_keycode(4) #back key
time.sleep(2)
driver.quit()