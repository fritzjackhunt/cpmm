import requests
import time
import json
import telebot  # or slackbot

def fetch_raydium_pairs():
    response = requests.get("https://api.raydium.io/v2/main/pairs")
    return response.json()

def check_for_new_pairs(current_pairs, new_pairs):
    new_pair_list = []
    for pair in new_pairs:
        if pair not in current_pairs:
            new_pair_list.append(pair)
    return new_pair_list

def send_telegram_notification(new_pairs):
     # Send notifications to Telegram channel
    bot = telebot.TeleBot('7077890021:AAG-rsFpkYQb8KnKjE6zUspHP6mhFI_sUvM')
    for pair in new_pairs:
        bot.send_message(5181134931, f"New pair: {pair}")

def main():
    current_pairs = fetch_raydium_pairs()
    while True:
        new_pairs = fetch_raydium_pairs()
        new_pair_list = check_for_new_pairs(current_pairs, new_pairs)
        if new_pair_list:
            send_telegram_notification(new_pair_list)
        current_pairs = new_pairs
        time.sleep(60)  # Adjust polling interval as needed

if __name__ == '__main__':
    main()
