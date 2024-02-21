from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

driver.implicitly_wait(8)
my_element = driver.find_element("id", "downloadButton")

my_element.click()

# progress = driver.find_element('class name','progress-label')
# print(f"{progress.text == 'Completed!'} ")

WebDriverWait(driver, 50).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),  # Element filtration
        'Complete!'  # The expected text

    )
)
