from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

driver.implicitly_wait(3)
my_element = driver.find_element("id", "downloadButton")

my_element.click()
