import requests
import time
from telegram import Bot
from telegram.ext import Updater, CommandHandler
import urllib3.contrib
from asyncio import Queue

# Replace with your bot token
TELEGRAM_BOT_TOKEN = '7077890021:AAG-rsFpkYQb8KnKjE6zUspHP6mhFI_sUvM'
TELEGRAM_CHAT_ID = '5181134931'


# Dexscreener API endpoint for new pairs (replace with actual endpoint)
DEXSCREENER_API_URL = "https://api.raydium.io/v2/main/pairs"

def fetch_new_pairs():
    response = requests.get(DEXSCREENER_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def send_telegram_message(bot: Bot, message: str):
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot is running...")

def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    my_queue = Queue()
    updater = Updater(bot=bot, update_queue=my_queue)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    
    updater.start_polling()

    last_seen_pairs = set()

    while True:
        new_pairs = fetch_new_pairs()
        if new_pairs:
            for pair in new_pairs['pairs']:
                pair_id = pair['id']
                if pair_id not in last_seen_pairs:
                    last_seen_pairs.add(pair_id)
                    message = f"New Pair Detected: {pair['baseToken']['symbol']} / {pair['quoteToken']['symbol']}\nPrice: {pair['priceUsd']}\nDex: {pair['dexName']}"
                    send_telegram_message(bot, message)
        
        time.sleep(60)  # Check every minute

if __name__ == '__main__':
    main()
