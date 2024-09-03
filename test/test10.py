from telethon import TelegramClient
from datetime import datetime, timedelta
import asyncio

# Replace with your own credentials
api_id = '20588411'  # Replace with your API ID
api_hash = '93edc28575ad46194e94f4a5997c5a02'  # Replace with your API Hash
channel_username = '@DSNewPairsSolana'  # Replace with the channel's username or ID

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()

    # Fetch messages from the last 30 minutes initially
    thirty_minutes_ago = datetime.now() - timedelta(minutes=30)
    messages = await client.get_messages(channel_username, offset_date=thirty_minutes_ago)

    # Print the fetched messages
    print(f"Messages from the last 30 minutes in {channel_username}:\n")
    for message in messages:
        print(f"{message.date.strftime('%Y-%m-%d %H:%M:%S')}: {message.text}\n")

    # Store the ID of the last message processed
    last_message_id = messages[-1].id if messages else None

    while True:
        # Fetch new messages since the last message ID
        new_messages = await client.get_messages(channel_username, min_id=last_message_id + 1)

        # Print the new messages
        if new_messages:
            # Sort new messages by date to ensure correct order
            new_messages.sort(key=lambda m: m.date)

            print(f"New messages received at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:\n")
            for message in new_messages:
                print(f"{message.date.strftime('%Y-%m-%d %H:%M:%S')}: {message.text}\n")

            # Update the last message ID to the most recent message processed
            last_message_id = new_messages[-1].id  # Update to the last new message's ID

        # Wait for a specified interval before checking again
        await asyncio.sleep(5)  # Check every 5 seconds

with client:
    client.loop.run_until_complete(main())