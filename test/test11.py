from telethon import TelegramClient, events
from datetime import datetime, timedelta

# Replace with your own credentials
api_id = '20588411'  # Replace with your API ID
api_hash = '93edc28575ad46194e94f4a5997c5a02'  # Replace with your API Hash
channel_username = '@DSNewPairsSolana'  # Replace with the channel's username or ID

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    message = event.message
    print(f"New message received at {message.date.strftime('%Y-%m-%d %H:%M:%S')}:\n")
    print(f"{message.date.strftime('%Y-%m-%d %H:%M:%S')}: {message.text}\n")

async def main():
    await client.start()

    # Fetch messages from the last 30 minutes initially
    thirty_minutes_ago = datetime.now() - timedelta(minutes=30)
    messages = await client.get_messages(channel_username, offset_date=thirty_minutes_ago)

    # Print the fetched messages
    print(f"Messages from the last 30 minutes in {channel_username}:\n")
    for message in messages:
        print(f"{message.date.strftime('%Y-%m-%d %H:%M:%S')}: {message.text}\n")

    # Run the event handler
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())