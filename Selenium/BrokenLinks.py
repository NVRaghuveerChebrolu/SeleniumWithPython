
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

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
all_links =driver.find_elements(By.TAG_NAME,'a')
print(f"Total number of links on the page:{len(all_links)}")
for link in all_links:
    url= link.get_attribute('href')
    print(url)
    # response = requests.head(href,allow_redirects=True,timeout=5)
    response = requests.get(url)
    if response.status_code>=400:
        print(f"Broken links:{url} (status code:{response.status_code})")
