from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

options = Options()
# options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)  # This is the key!
driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
dropdownInHerokuapp = driver.find_element(By.ID,"dropdown")
select = Select(dropdownInHerokuapp)
# select.select_by_index(2)
# select.select_by_value('Option 2')
select.select_by_visible_text('Option 2')
NumberOfDropDowns = len(select.options)
print(NumberOfDropDowns)
expectedCount =3
if NumberOfDropDowns==expectedCount:
    print("DropDownSateCount is correct")
else:
    print("DropDownSateCount is not correct")

DropDownValueToSelect = "Option 1"
for option in select.options:
    if option.text==DropDownValueToSelect:
        option.click()
        print(f"selected option is {DropDownValueToSelect}")
        break
    else:
        print(f"selected option is {DropDownValueToSelect} not found")