from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# browser = webdriver.Chrome
# browser.get("https://selenium.dev/")
# browser.maximize_window()
options = Options()
# options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)  # This is the key!
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
# driver.execute_script("window.scrollTo(0,document.body.);")
element = driver.find_element(By.ID,"hobbies-checkbox-1")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
checkBoxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkBoxes:
    # checkbox.click()
    checkbox.send_keys(Keys.SPACE)

checked_count =0
for checkbox in checkBoxes:
    if(checkbox.is_selected()):
        checked_count+=1

expectedChecked_Count=3
if checked_count==expectedChecked_Count:
    print('check box count is verified')
else:
    print('checkbox count is not verified')




