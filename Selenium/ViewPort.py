import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

viewports =[(1024,768),(768,1024),(375,667),(414,816)]
options = Options()
options.add_experimental_option("detach", True)  # This is the key!
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/")
try:
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(5)
finally:
    driver.close()
