from telethon import TelegramClient, events
import requests
import asyncio

# Telegram bot credentials
api_id = '20588411'
api_hash = '93edc28575ad46194e94f4a5997c5a02'
bot_token = '7077890021:AAG-rsFpkYQb8KnKjE6zUspHP6mhFI_sUvM'
channel_id = 'cpmmdex'  # ID of the channel you want to send messages to

# GraphQL query to fetch Raydium pools
query = """
{
  pools {
    id
    name
    type
    liquidity
    volume24h
  }
}
"""

# GraphQL endpoint for The Graph
graph_url = 'https://api.thegraph.com/subgraphs/name/raydium-io/raydium'

# Initialize Telegram Client
client = TelegramClient('raydium_bot', api_id, api_hash).start(bot_token=bot_token)

# Function to fetch data from The Graph
async def fetch_pools():
    response = requests.post(graph_url, json={'query': query})
    if response.status_code == 200:
        return response.json()['data']['pools']
    else:
        print("Failed to fetch data from The Graph")
        return []

# Function to filter CPMM pools and send notifications
async def check_and_notify():
    # Fetch pools
    pools = await fetch_pools()
    
    for pool in pools:
        if 'cpmm' in pool['type'].lower():  # Check if it's a CPMM pool
            message = f"New CPMM Pool Listed:\n\nName: {pool['name']}\nLiquidity: {pool['liquidity']}\nVolume 24h: {pool['volume24h']}"
            
            # Send message to the Telegram channel
            await client.send_message(channel_id, message)

# Schedule to check for new pools every 5 minutes
async def main():
    while True:
        await check_and_notify()
        await asyncio.sleep(300)  # Wait for 5 minutes before checking again

with client:
    client.loop.run_until_complete(main())