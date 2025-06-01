
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

driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,700)")
table = driver.find_element(By.XPATH,"//table[@id='countries']")
rows = driver.find_elements(By.XPATH,"//table[@id='countries']/tbody/tr")
rows_count = len(rows)
print(rows_count)
text_to_find="Germany"
found = False
for row_index, row in enumerate(rows):
    cells = row.find_elements(By.TAG_NAME,"td")
    for col_index, cell in enumerate(cells):
        if text_to_find==cell.text:
            found=True
            print(f"Target_value {text_to_find} found in row:{row_index} and cell:{col_index}")
            break
    if found:
        break
    else:
        print(f"Target_value {text_to_find} not found at row:{row_index}")


