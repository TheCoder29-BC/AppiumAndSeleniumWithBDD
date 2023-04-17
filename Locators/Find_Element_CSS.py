"""
Below are some of the ways to find WebElement using CssSelector

1. To write id name in css selector you need to add "#" before id value

2. to write class name in css selector you need to add "." before class name

3. Using " Tag name("input") and name " Attribute value as css_selector

4. Using " Tag name("input"),className and name " Attribute value as css_selector

5. "^" - Find elements using starts with a string value

6. "$" - Find elements using Ends with a string value

7. "*" - Find elements using contains a substring.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.dummypoint.com/seleniumtemplate.html") #Uses to launch the webpage

time.sleep(5)

# 1. Using ID name in CSS Selector (To Write id name in css selector you need to add "#" before id value)
driver.find_element(By.CSS_SELECTOR,"#user_input").send_keys("Code2Break_Id") #->#htmlid

# 2. Using Class name in CSS Selector(To write class name in css selector you need to add "." before class name)
driver.find_element(By.CSS_SELECTOR,".entertext").send_keys("Code2Break_ClassName") #->#html clas name

# 3. Using " Tag name("input") and name " Attribute value as css_selector
driver.find_element(By.CSS_SELECTOR,".input[name=textbox]").send_keys("Code2Break_TagName") #->#html clas name

# 4. Using " Tag name("input"),className and name " Attribute value as css_selector
driver.find_element(By.CSS_SELECTOR,".input.entertext[name=textbox]").send_keys("Code2Break_TagClassNameAndName")
# 5. "^" - Find elements using starts with a string value
driver.find_element(By.CSS_SELECTOR,"input[class^='en'").send_keys("Code2Break_StartingLetterUsingClassName")

# 6. "$" - Find elements using Ends with a string value min.char are 2
driver.find_element(By.CSS_SELECTOR,"input[class$='xt'").send_keys("Code2Break_EndsletterUsingClass")

# 7. "*" - Find elements using contains a substring.
driver.find_element(By.CSS_SELECTOR,"input[class*='ter']").send_keys("Code2Break_SubstringUsingofAClassName")

time.sleep(5)

driver.quit()