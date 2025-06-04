import time
from datetime import datetime,timedelta

import driver
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
# options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)  # This is the key!
driver = webdriver.Chrome(options=options)
url="https://demo.automationtesting.in/Datepicker.html"
driver.get(url)
driver.maximize_window()
time.sleep(5)
# Mouse Over Operation
actions = ActionChains(driver)
hoverElement= driver.find_element(By.XPATH,"//a[normalize-space()='SwitchTo']")
actions.move_to_element(hoverElement).perform()
actions.click(driver.find_element(By.XPATH,"//a[normalize-space()='Frames']")).perform()

# Drag and Drop Operation
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
drag_source= driver.find_element(By.ID,"column-a")
drop_destination= driver.find_element(By.ID,"column-b")
actions.drag_and_drop(drag_source,drop_destination).perform()
