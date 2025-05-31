import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# browser = webdriver.Chrome
# browser.get("https://selenium.dev/")
# browser.maximize_window()
options = Options()
options.add_experimental_option("detach", True)  # This is the key!
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
driver.close()