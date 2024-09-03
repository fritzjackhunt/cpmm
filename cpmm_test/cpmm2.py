from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Disable sandbox mode

# Path to your ChromeDriver
service = Service('/usr/bin/chromedriver')  # Update this to your driver's path

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Dexscreener
driver.get("https://dexscreener.com/new-pairs?rankBy=pairAge&order=asc&chainIds=solana&dexIds=raydium&minLiq=10000")

# Wait for the page to load completely (adjust time as needed)
time.sleep(5)  # You might need to increase this depending on the page load time

# Scroll down the page if necessary to load more data
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)  # Wait for additional content to load

# Get the page source and parse it with BeautifulSoup
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')

# Find all CPMM tokens - you'll need to replace 'cpmm-token-class' with the actual class or identifier
cpmm_tokens = soup.find_all('span', class_='ds-dex-table-row-badge-label')  # Update with correct class name

# Extract and print token names
new_tokens = [token.text.strip() for token in cpmm_tokens]
print(f"Found CPMM tokens: {new_tokens}")

# Close the browser
driver.quit()