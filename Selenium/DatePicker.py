import time
from datetime import datetime,timedelta

import driver
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
url="https://www.globalsqa.com/demo-site/datepicker/"
driver.get(url)
driver.maximize_window()
time.sleep(5)
iframe = driver.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(iframe)
time.sleep(3)
driver.find_element(By.ID,"datepicker").click()
current_date =datetime.now()
print(f"current date is :{current_date}")
nextDate =current_date+timedelta(days=1)
formatted_date= nextDate.strftime("%m/%d/%y")
print(f"formated date is :{formatted_date}")
driver.find_element(By.ID,"datepicker").send_keys(formatted_date+Keys.TAB)

driver.switch_to.default_content()

# drop down date picker
print("Drop Down Date Picker")
driver.get("https://demo.automationtesting.in/Datepicker.html")
time.sleep(5)
driver.find_element(By.ID,"datepicker2").click()
time.sleep(5)
current_date=datetime.now()
print(f"current_date:{current_date}")

next_day=current_date+timedelta(days=1)
print(f"next_day:{next_day}")
dayinNextDay=(str(next_day.day))
print(f"dayinNextDay:{dayinNextDay}")
currentMonth=datetime.now().month
currentYear=current_date.year

nextMonth =(currentMonth%12)+1
next_month_year =f"{nextMonth}/{currentYear}"
Month_Dropdown= driver.find_element(By.CSS_SELECTOR,"select[title='Change the month']")
select = Select(Month_Dropdown)
select.select_by_value(str(next_month_year))
year_Dropdown=driver.find_element(By.CSS_SELECTOR,"select[title='Change the year']")
select = Select(year_Dropdown)
select.select_by_visible_text("2024")
driver.find_element(By.LINK_TEXT,dayinNextDay).click()
time.sleep(5)



