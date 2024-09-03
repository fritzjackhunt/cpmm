import json
import requests
import websocket

# Replace with your actual values
TELEGRAM_BOT_TOKEN = '7077890021:AAG-rsFpkYQb8KnKjE6zUspHP6mhFI_sUvM'
CHAT_ID = '5181134931'
RADIO_URL = 'wss://api.radium.io/v2/pool'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    requests.post(url, data=payload)

def on_message(ws, message):
    data = json.loads(message)
    # Check for new pool creation
    if 'method' in data and data['method'] == 'newPool':
        pool_info = data['params']
        token_name = pool_info['name']
        token_address = pool_info['address']
        message = f"New Token Listed on Radium: {token_name}\nAddress: {token_address}"
        send_telegram_message(message)

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")

if __name__ == "_main_":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(RADIO_URL,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()