import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import time

# Slack configuration
SLACK_BOT_TOKEN = 'your_slack_bot_token'
SLACK_CHANNEL = '#your_channel'

# Dexscreener API endpoint for Raydium pairs (replace with actual endpoint)
DEXSCREENER_API_URL = 'https://api.dexscreener.com/latest/dex/pairs/raydium'

client = WebClient(token=SLACK_BOT_TOKEN)

def fetch_new_pairs():
    response = requests.get(DEXSCREENER_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def send_slack_message(channel, message):
    try:
        response = client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        assert e.response["error"]

def main():
    last_seen_pairs = set()

    while True:
        new_pairs = fetch_new_pairs()
        if new_pairs:
            for pair in new_pairs['pairs']:
                pair_id = pair['id']
                if pair_id not in last_seen_pairs:
                    last_seen_pairs.add(pair_id)
                    message = f"New Pair Detected: {pair['baseToken']['symbol']} / {pair['quoteToken']['symbol']}\nPrice: {pair['priceUsd']}\nDex: {pair['dexName']}"
                    send_slack_message(SLACK_CHANNEL, message)
        
        time.sleep(60)  # Check every minute

if __name__ == '__main__':
    main()
