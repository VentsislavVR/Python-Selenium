from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

sum1 = driver.find_element("id", "value1")
sum2 = driver.find_element("id", "value2")
driver.implicitly_wait(5)

sum1.send_keys(15)
sum2.send_keys(15)

# driver.implicitly_wait(8)
# my_element = driver.find_element("id", "value1")
# my_element.send_keys("10")
#
# my_element = driver.find_element("id", "value2")
# my_element.send_keys("20")
#
# my_element = driver.find_element("id", "btn btn-primary")
# my_element.click()
#
# WebDriverWait(driver, 50).until(
#     EC.text_to_be_present_in_element(
#         (By.CLASS_NAME, 'displayvalue'),  # Element filtration
#         '30'  # The expected text
#
#     )
# )
