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

# Extract CPMM tokens (assuming there's a specific class or tag that identifies them)
# Adjust the following line according to the actual structure you find in the developer tools
cpmm_tokens = soup.find_all('span', class_='ds-dex-table-row-badge ds-dex-table-row-badge-label') # Replace with the actual class name

# Process tokens
new_tokens = []
for token in cpmm_tokens:
    token_name = token.text.strip()
    new_tokens.append(token_name)

# Compare with previous tokens (you'll need to store these somewhere)
previous_tokens = [...]  # Load from a file or database

# Find new tokens
new_cpmm_tokens = set(new_tokens) - set(previous_tokens)

# Notify if there are new tokens
if new_cpmm_tokens:
    # Send a notification (email, SMS, etc.)
    print(f"New CPMM Tokens found: {new_cpmm_tokens}")
    # Update the previous tokens list
    previous_tokens = new_tokens
else:
    print("No new CPMM tokens found.")

# Save the updated tokens list for future comparison
# Save previous_tokens to a file or database for the next run

time.sleep(600)  # Run the script every 10 minutes