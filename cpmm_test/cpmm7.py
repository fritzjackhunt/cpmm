import requests
from urllib.parse import urlencode

# Set your ScraperAPI key
API_KEY = 'e9c213f968789abf8f52a463d7d77e84'

# URL you want to scrape
url = 'https://dexscreener.com/new-pairs?rankBy=pairAge&order=asc&chainIds=solana&dexIds=raydium&minLiq=10000'

# Set ScraperAPI parameters
params = {
    'api_key': API_KEY,
    'url': url,
    'render': 'true',  # Render JavaScript if needed
    'country_code': 'us',  # Specify country for geo-targeting
    #'premium': 'true'  # Use premium proxies for better success rate
}

# Send request to ScraperAPI
response = requests.get('http://api.scraperapi.com/', params=urlencode(params))

# Check if request was successful
if response.status_code == 200:
    # Extract relevant data from the response
    html_content = response.text
    # Process the HTML content as needed
    print(html_content)
else:
    print(f'Request failed with status code: {response.status_code}')