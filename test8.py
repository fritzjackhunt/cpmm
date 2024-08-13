from telethon import TelegramClient
from datetime import datetime
import asyncio  # Ensure asyncio is imported

# Replace with your own credentials
api_id = '20588411'  # Replace with your API ID
api_hash = '93edc28575ad46194e94f4a5997c5a02'  # Replace with your API Hash
channel_username = '@DSNewPairsSolana'  # Replace with the channel's username or ID
message_limit = 10  # Set the number of latest messages to retrieve

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()
    
    # Fetch the latest messages
    messages = await client.get_messages(channel_username, limit=message_limit)
    
    # Print the latest messages
    print(f"Latest {message_limit} messages from {channel_username}:\n")
    for message in messages:
        print(f"{message.date.strftime('%Y-%m-%d %H:%M:%S')}: {message.text}\n")
    
    # Store the timestamp of the latest message
    latest_message_timestamp = messages[0].date
    
    while True:
        # Fetch new messages since the latest message
        new_messages = await client.get_messages(channel_username, offset_date=latest_message_timestamp)
        
        # Print the new messages
        if new_messages:
            print(f"New messages received at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:\n")
            for message in new_messages:
                print(f"{message.date.strftime('%Y-%m-%d %H:%M:%S')}: {message.text}\n")
            
            # Update the latest message timestamp
            latest_message_timestamp = new_messages[0].date
        
        # Wait for 60 seconds before checking for new messages again
        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(main())