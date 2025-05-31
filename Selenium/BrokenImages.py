
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

driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()
all_Images =driver.find_elements(By.TAG_NAME,"img")
print(f"Total number of images on the page:{len(all_Images)}")
broken_images=[]
for image in all_Images:
    src= image.get_attribute('src')
    print(src)
    if src:
        response = requests.get(src)
        if response.status_code!=200:
            broken_images.append(src)
            print(f"Broken images found")
if broken_images:
    print("list of broken images:")
    for brokenImg in broken_images:
        print(brokenImg)