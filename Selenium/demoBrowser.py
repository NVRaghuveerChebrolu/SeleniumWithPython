import time
from selenium import webdriver

#chrome driver service. It check the chrome broswer version and it goes to the internet nad download the driver
#library and install it for you . all this happens very fast
driver = webdriver.Chrome()
time.sleep(4)
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)