#How we get the Webtable
"""
----- Links -----
https://www.youtube.com/watch?v=oMmxcz94ugg&ab_channel=qavbox
https://qavalidation.com/2021/01/automate-handle-web-table-using-selenium-python.html/

example Webtable
https://qavbox.github.io/demo/webtable/
Webtable.png

-----------------
"""


from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.support.select import Select
import time

#Syntax  1
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#Sytnax 2
#driver = webdriver.Chrome(executable_path="C:/Users/HW/Documents/Appium/AndroidDemoApp-main/ChromeDriver/chromedriver.exe")

driver.get("https://qavbox.github.io/demo/webtable/") #Uses to launch the webpage

time.sleep(5)

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])


#inspect the table
"""
tbody is complete the Table Body and below of them the <tr> ar the rows
example:
    <table class="table">
    <thead>
        <th>
    <tbody>
        <td>
"""

assert "webtable" in driver.title

Webtable = driver.find_element(By.XPATH,"table01")
Webtable_Header = Webtable.find_elements(By.TAG_NAME,"th")
"""
for headerElements in Webtable_Header:
    print(headerElements.text)
   
    --- Output ---
    ManualTesting
    AutomationTesting
    IssueTracker
    
"""
Webtable_cells = Webtable.find_elements(By.TAG_NAME,"td")
"""
for cells in Webtable_cells:
    print(cells.text)

    --- Output ---
    Functional
    QTP
    Bugzilla
    
    
    GUI
    Selenium
    TFS
    
    
    Performance
    Coded UI
    QC ALM
    

"""
Webtable_body = Webtable.find_elements(By.TAG_NAME,"tbody")

Webtable_rows = Webtable.find_elements(By.TAG_NAME,"tr")
"""
for body in Webtable_body:
    print(body.text)
 
     --- Output ---
     
    ManualTesting
    AutomationTesting
    IssueTracker
    
    Functional
    QTP
    Bugzilla
    
    
    GUI
    Selenium
    TFS
    
    
    Performance
    Coded UI
    QC ALM
    
    Functional QTP Bugzilla
    GUI Selenium TFS
    Performance Coded UI QC ALM


   
"""
#see how many row they had
print(len(Webtable_rows))

#delete one row and see the length of rows
#we will the delete the row with TFS
for i in range(len(Webtable_rows)):
    Webtable_columns = Webtable_rows[i].find_elements(By.TAG_NAME,"td") # cuase each row has his own td
    for j in range(len(Webtable_columns)):
        if Webtable_columns[j].text == "TFS":
            Webtable_columns[0].click() #the checkbox is in column 0 and we will click on it

time.sleep(15)
#Simple Way
print(driver.find_elements(By.XPATH,"//table['@id=table01']"))
#to specific rows and columns with xPath
#//table['table@id=table01']/tbody/tr[2]/td[2]
print(driver.find_elements(By.XPATH,"//table['table@id=table01']/tbody/tr[2]/td[2]").text)
Webtable_link = driver.find_elements(By.XPATH,"//table['table@id=table01']/tbody/tr[2]/td[2]")
Webtable_link.click()

driver.quit()

