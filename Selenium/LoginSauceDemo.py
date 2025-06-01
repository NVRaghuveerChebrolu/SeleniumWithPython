from optparse import Option

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
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
title=driver.title
print(title)
assert "Swag Labs" in title
userName = "standard_user"
passWord = "secret_sauce"
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys(userName)
passSuseDemo = driver.find_element(By.ID,"password")
passSuseDemo.send_keys(passWord)
loginButton = driver.find_element(By.XPATH,"//input[@id='login-button']")
assert not loginButton.get_attribute("disabled")
loginButton.click()

elementProductPresent=driver.find_element(By.XPATH,"//span[@class='title']").text
assert elementProductPresent=="Products"

input("Press Enter to close the browser...")