from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()

options.headless = True

driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options)

driver.get("https://google.com/")
print(driver.title)
driver.quit()