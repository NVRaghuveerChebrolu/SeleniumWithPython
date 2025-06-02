import time

import driver
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
# options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)  # This is the key!
driver = webdriver.Chrome(options=options)
url="https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)
driver.maximize_window()

buttonJsAlert = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
buttonJsAlert.click()
jsAlert = driver.switch_to.alert
Text_jsAlert=jsAlert.text
time.sleep(4)
jsAlert.accept()

buttonJsConfirmAlert = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
buttonJsConfirmAlert.click()
jsConfirmAlert = driver.switch_to.alert
Text_ConfirmAlert=jsConfirmAlert.text
time.sleep(4)
jsAlert.dismiss()
textOfConformAlertResult = driver.find_element(By.XPATH,"//p[@id='result']").text
print(f"message displayed for conform box alert:{textOfConformAlertResult}")

buttonJsPromptAlert = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
buttonJsPromptAlert.click()
jsPromptAlert = driver.switch_to.alert
jsPromptAlert.send_keys("i am inside prompt box alert")
jsAlert.accept()
textOfPromptResult = driver.find_element(By.XPATH,"//p[@id='result']").text
print(f"message displayed for prompt box alert:{textOfPromptResult}")



