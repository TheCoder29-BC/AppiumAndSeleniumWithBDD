"""
1. Absolute XPath:
It uses from complete html root path to the required WebElement.
EX :/html/body/div[1]/div/div[3]/section/div[2]/div/form/input[1] (or) //*[@id="user_input"]

'/'  - finding the element inside the parent element
'//' - finding the child or nested-child element inside the parent element

2. Relative XPath:
It uses the direct path of a WebElement using (id,className,attribute values, sub-string,etc) to perform action on it.

    I.)  EX : //tag[@attribute='value']
            "//*[@id="user_input"]" or "//input[@id="user_input"]"

    II.) Using Contains ( Need to give partial value) :
        Syntax : "//tag[contains(@attribute,'partial value ıf attribute')]"
        Ex :     ""//input[contains(@id,"user"] , "//a[contains(text(), 'Form']"

    III.) Starts-with ( Need to give partial value) :
          Syntax : "//tag[starts-with(@attribute,'partial value of attribute')]"
          Ex :     "//input[starts-with(@id,'user')]"


"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.dummypoint.com/seleniumtemplate.html") #Uses to launch the webpage

time.sleep(5)

driver.find_element(By.XPATH,"//a[contains(text(),'Form')]").click()

driver.quit()