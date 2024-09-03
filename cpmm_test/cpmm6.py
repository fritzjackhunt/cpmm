from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

driver.get("https://python.org")
print(driver.title)
driver.close()