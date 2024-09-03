import requests
from bs4 import BeautifulSoup
import time

# Define the URL to scrape
url = "https://dexscreener.com/new-pairs?rankBy=pairAge&order=asc&chainIds=solana&dexIds=raydium&minLiq=10000"

# Fetch the page content
response = requests.get(url)
html_content = response.content

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

print(soup.prettify())