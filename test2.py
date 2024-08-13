import requests
import time
import logging
from telegram import Bot

# Set up logging
logging.basicConfig(level=logging.INFO)

# Dexscreener API endpoint
api_url = "https://api.dexscreener.com/latest/dex/pairs/:chainId/:pairAddresses"

# Your Telegram bot token
bot_token = "7077890021:AAG-rsFpkYQb8KnKjE6zUspHP6mhFI_sUvM"
bot = Bot(token=bot_token)

# Your Telegram chat ID
chat_id = "5181134931"

# Time interval for checking new listings (in seconds)
check_interval = 60  # e.g., check every minute

# Store the latest pairs to avoid duplicate notifications
tracked_pairs = set()

def fetch_latest_pairs():
    logging.info("Fetching latest pairs from Dexscreener.")
    response = requests.get(api_url)
    response.raise_for_status()  # Ensure we get a valid response
    data = response.json()
    logging.info(f"Fetched {len(data['pairs'])} pairs.")
    return data['pairs']

def notify_new_listing(pair):
    message = f"New CPMM listing found: {pair['name']} at {pair['url']}"
    logging.info(f"Sending notification: {message}")
    bot.send_message(chat_id=chat_id, text=message)
    logging.info("Notification sent.")

def main():
    logging.info("Bot started. Monitoring new CPMM listings on Solana.")
    while True:
        try:
            pairs = fetch_latest_pairs()
            for pair in pairs:
                    notify_new_listing(pair)
                    tracked_pairs.add(pair['address'])
        except Exception as e:
            logging.error(f"Error fetching or processing pairs: {e}")

        # Wait for the next check
        time.sleep(check_interval)

if __name__ == "__main__":
    main()
