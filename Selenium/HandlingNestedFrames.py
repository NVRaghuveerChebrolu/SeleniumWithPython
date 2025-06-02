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

driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.maximize_window()
# switching to top frame
driver.switch_to.frame("frame-top")
# switching to middle frame
driver.switch_to.frame("frame-middle")
contentOfMiddleFrame = driver.find_element(By.ID,"content").text
print("content in the middle frame:"+contentOfMiddleFrame)
driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")
contentOfBottomFrame = driver.find_element(By.TAG_NAME,"body").text
print("content in the bottom frame:"+contentOfBottomFrame)
driver.switch_to.default_content()


