from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode

# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options)

# Navigate to a website
driver.get("https://dexscreener.com/new-pairs?rankBy=pairAge&order=asc&chainIds=solana&dexIds=raydium&minLiq=10000")


# Find a span element using XPath with text()
span_element = driver.find_element_by_xpath("//span[text()='CPMM']")
print(span_element.text)

#print(element.text)

# Close the browser
driver.quit()