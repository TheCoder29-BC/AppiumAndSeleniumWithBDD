#First check the Chrome Version ---->chrome://settings/help
#then download the chromedriver
import time

#take the chromedriver path for old Selenium also possible
#C:\Users\HW\Documents\Appium\AndroidDemoApp-main\ChromeDriver\chromedriver.exe

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.dummypoint.com/seleniumtemplate.html") #Uses to launch the webpage

time.sleep(5)
#ID
driver.find_element(By.ID,"user_input").send_keys("Test2Test3Test")

#Classname
driver.find_element(By.CLASS_NAME,"entertext").send_keys("Test")

#name
driver.find_element(By.NAME,"radio").click()

#tag-Name
driver.find_element(By.TAG_NAME,"input").send_keys("Tag_Name")

#Link text <a href="..">
driver.find_element(By.LINK_TEXT,"FORM").click()

#Partial Link it find the Form.html and click on it
driver.find_element(By.PARTIAL_LINK_TEXT,"FOR").click()


time.sleep(5)

driver.quit()
