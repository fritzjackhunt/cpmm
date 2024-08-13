from telethon import TelegramClient, events
from datetime import datetime, timedelta
import re

# Replace with your own credentials
api_id = '20588411'  # Replace with your API ID
api_hash = '93edc28575ad46194e94f4a5997c5a02'  # Replace with your API Hash
source_channel_username = '@DSNewPairsSolana'  # Replace with the channel's username or ID
target_channel_username = '@cpmmdex'

# Patterns to filter out (adjust the patterns as needed)
filter_patterns = [r'.pump.', 'meteora', 'orca', r'.*pattern.']  # Replace with the patterns you want to filter out

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel_username))
async def handler(event):
    message = event.message
    message_text = message.text.lower()  # Convert message text to lower case for case-insensitive matching

    # Check if the message matches any of the filter patterns
    if any(re.search(pattern, message_text) for pattern in filter_patterns):
        return  # Skip printing this message

    # Check if the message contains "Total liquidity:" and the value is greater than 10,000
    liquidity_match = re.search(r'total liquidity:\s*\*\*\s*\$\s*([\d,]+)\s*\*\*', message_text)
    if liquidity_match:
        liquidity_value = int(liquidity_match.group(1).replace(',', ''))
        if liquidity_value <= 10000:
            return  # Skip printing this message
        
    # Check if the message contains "FDV:" and the value is greater than 500,000
    fdv_match = re.search(r'fdv:\s*\\\s*\$\s*([\d,]+)\s*\\', message_text)
    if fdv_match:
        fdv_value = int(fdv_match.group(1).replace(',', ''))
        if fdv_value < 300000:
            return False  #Skip printin this message

    #Send the filtered message to the target channel
    await client.send_message(target_channel_username, message.text)

async def main():
    await client.start()

    # Fetch messages from the last 30 minutes initially
    thirty_minutes_ago = datetime.now() - timedelta(minutes=30)
    messages = await client.get_messages(source_channel_username, offset_date=thirty_minutes_ago)

    # Print the fetched messages
    print(f"Messages from the last 30 minutes in {source_channel_username}:\n")
    for message in messages:
        message_text = message.text.lower()  # Convert message text to lower case for case-insensitive matching

        if any(re.search(pattern, message_text) for pattern in filter_patterns):
            continue  # Skip printing this message

        # Check if the message contains "Total liquidity:" and the value is greater than 10,000
        liquidity_match = re.search(r'total liquidity:\s*\*\*\s*\$\s*([\d,]+)\s*\*\*', message_text)
        if liquidity_match:
            liquidity_value = int(liquidity_match.group(1).replace(',', ''))
            if liquidity_value <= 10000:
                continue  # Skip printing this message

        #Send the filtered message to the target channel
        await client.send_message(target_channel_username, message.text)

    # Run the event handler
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())