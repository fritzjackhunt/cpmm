import requests
import time
import logging
from telegram import Bot

# Set up logging
logging.basicConfig(level=logging.INFO)

# Your Telegram bot token
bot_token = '7077890021:AAG-rsFpkYQb8KnKjE6zUspHP6mhFI_sUvM'
bot = Bot(token=bot_token)

# Your Telegram chat ID
chat_id = '5181134931'

# Raydium API endpoint (this is an example, make sure it's correct)
api_url = "https://api.raydium.io/v2/main/pairs"

# Time interval for checking new listings (in seconds)
check_interval = 300  # e.g., check every 5 minutes

# Store the latest pairs to avoid duplicate notifications
tracked_pairs = set()

def fetch_latest_pairs():
    logging.info("Fetching latest pairs from Raydium.")
    response = requests.get(api_url)
    response.raise_for_status()  # Ensure we get a valid response
    data = response.json()
    return data

def notify_new_listing(pair):
    message = f"New Raydium v3 listing found: {pair['name']} at {pair['url']}"
    logging.info(f"Sending notification: {message}")
    bot.send_message(chat_id=chat_id, text=message)
    logging.info("Notification sent.")

def main():
    logging.info("Bot started. Monitoring new Raydium v3 listings.")
    while True:
        try:
            pairs = fetch_latest_pairs()
            for pair in pairs:
                pair_id = pair['id']  # Adjust this according to the actual structure
                if pair_id not in tracked_pairs:
                    notify_new_listing(pair)
                    tracked_pairs.add(pair_id)
        except Exception as e:
            logging.error(f"Error fetching or processing pairs: {e}")

        # Wait for the next check
        time.sleep(check_interval)

if __name__ == "_main_":
    main()