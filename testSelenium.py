from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://selenium.dev/')
driver.quit()