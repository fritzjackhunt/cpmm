from telethon import TelegramClient

# Replace with your own credentials
api_id = '20588411'
api_hash = '93edc28575ad46194e94f4a5997c5a02'
channel_username = '@DSNewPairsSolana'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()
    async for message in client.iter_messages(channel_username):
        print(message.sender_id, message.text)

with client:
    client.loop.run_until_complete(main())