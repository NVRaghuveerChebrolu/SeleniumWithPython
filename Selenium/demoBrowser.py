import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

#chrome driver service. It check the chrome broswer version and it goes to the internet nad download the driver
#library and install it for you . all this happens very fast

# service_obj = Service("/Users/dell/downloads/chromedriver.exe")
# driver = webdriver.chrome(service= service_obj)
# driver = webdriver.Firefox(service_obj)
# driver = WebDriver.Edge(service=service_obj)

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

#how to fill the form
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
#  css for id is #id   css for class is .classname
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Raghu")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
driver.find_element(By.XPATH,"//input[@class='btn btn-success']").click()
time.sleep(4)
successMessage=driver.find_element(By.CLASS_NAME,"alert-success").text
print(successMessage)
assert "Success" in successMessage



