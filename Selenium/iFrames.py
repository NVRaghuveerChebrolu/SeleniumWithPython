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

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@aria-label='Close']").click()
iframe = driver.find_element(By.ID,"mce_0_ifr")
wait = WebDriverWait(driver, 10)
# wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "frame1")))
driver.switch_to.frame(iframe)
TextEditor = driver.find_element(By.ID,"tinymce")
TextEditor.clear()
TextEditor.send_keys("text box inside iframe")
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//a[text()='Elemental Selenium']").click()

