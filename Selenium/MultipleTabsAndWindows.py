
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import requests
options = Options()
# options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)  # This is the key!
driver = webdriver.Chrome(options=options)

driver.get("https://www.selenium.dev/")
driver.maximize_window()
driver.switch_to.new_window()
driver.get("https://playwright.dev/")
number_of_Tabs=len(driver.window_handles)
print(number_of_Tabs)
tabs_value = driver.window_handles
print(tabs_value)
current_tab=driver.current_window_handle
print(current_tab)
driver.find_element(By.CSS_SELECTOR,".getStarted_Sjon").click()
FirstTab= driver.window_handles[0]
if current_tab != FirstTab:
    driver.switch_to.window(FirstTab)
    driver.find_element(By.XPATH,"//span[normalize-space()='Downloads']").click()