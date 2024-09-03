from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up Chrome options
options = Options()
#options.add_argument("--headless")  # Run in headless mode

# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options)

# Navigate to a website
driver.get("https://selenium-python.readthedocs.io/locating-elements.html")

try: 
    content = driver.find_element(By.CSS_SELECTOR, 'div.highlight-default')
    print("Found content", content)
except Exception as e:
    print("Error finding content", e)


# Close the browser
driver.quit()