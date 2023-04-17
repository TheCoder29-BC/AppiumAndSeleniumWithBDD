from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException,ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.common.alert import Alert

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.dummypoint.com/Windows.html") #Uses to launch the webpage
assert "Selenium Template" in driver.title
time.sleep(5)

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

# To get the current window name
WindowName = driver.current_window_handle
print("Before Switching",WindowName)

# click on popup button to open new window
Element = driver.find_elements(By.TAG_NAME,"input")
for popup_buttons in Element:
    popup_button = popup_buttons.get_attribute("value")
    if popup_button == "Open a Popup Window2":
        popup_buttons.click()

time.sleep(2)
# Print the list of windows are presen on the screen in present session

windows = driver.window_handles
for window in windows:
    print(window)
"""
Output

CDwindow-732F7D80A27168AA22ADC030F2A32480
CDwindow-732F7D80A27168AA22ADC030F2A32480
CDwindow-E25C302B5CBE20A41B0C13CA251FBFE5

"""
# switch to required window
driver.switch_to.window(windows[1])

WindowName = driver.current_window_handle
print("After switching ",WindowName)

driver.maximize_window()
"""
Here switching to new window and performing action frame
"""
time.sleep(2)

Element_Frame = driver.find_element(By.ID,"f2")
driver.switch_to.frame(Element_Frame)

DaTa = driver.find_element(By.ID,"framename")
print("Frame Name is : ",DaTa.text)

time.sleep(3)
driver.close()

time.sleep(5)
driver.quit()

"""
Output

Before Switching CDwindow-FAB86533C5B2284E2C3D58C07EAAB329
CDwindow-FAB86533C5B2284E2C3D58C07EAAB329
CDwindow-F14965F5799B13668EE7D3DC1AE74AB3
After switching  CDwindow-F14965F5799B13668EE7D3DC1AE74AB3
Frame Name is :  Frame 2

"""