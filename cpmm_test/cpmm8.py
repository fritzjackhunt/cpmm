import requests
from bs4 import BeautifulSoup

payload = {
    'api_key': 'e9c213f968789abf8f52a463d7d77e84', 
    'url': 'https://dexscreener.com/new-pairs?rankBy=pairAge&order=asc&chainIds=solana&dexIds=raydium&minLiq=10000'}

html = requests.get('http://api.scraperapi.com', params=payload)

soup = BeautifulSoup(html.text, "lxml")
soup = soup.select(".ds-dex-table-row-badge-label")

print(soup)
