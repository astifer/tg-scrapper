from dotenv import load_dotenv
import os

import atexit
import datetime 
from telethon.sync import TelegramClient
from telethon.tl.types import User, Channel, Message
from telethon import functions, types

from util import get_list_of_chanels, is_today, get_prefix_for_chanels
from ml import create_summary

load_dotenv()

api_token = os.getenv('API_TOKEN')
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

client = TelegramClient('session', api_id, api_hash)
list_of_chanels = get_list_of_chanels()
prefixes = get_prefix_for_chanels()

async def main():
    # Connect to Telegram
    await client.start()

    result = {}
    # Get messages from the specified channel
    for chanel in list_of_chanels:
        msgs_for_chanel = []
        async for message in client.iter_messages(chanel, limit=10):
            if is_today(message.date) and len(message.text) > 250:
                msgs_for_chanel.append(message.text)
        
        if msgs_for_chanel:
            result[chanel] = msgs_for_chanel
            
        print(f"for chanel {chanel} found {len(msgs_for_chanel)} messages")
        
    for chanel in result:
        summary = create_summary(result[chanel][0])
        print(f"For chanel {chanel} last post summary:\n {summary}")
        

with client:
    client.loop.run_until_complete(main())