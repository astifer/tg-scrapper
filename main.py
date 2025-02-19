from dotenv import load_dotenv
import os

import datetime 
from telethon.sync import TelegramClient

from util import get_list_of_chanels, is_today, get_prefix_for_chanels, get_config
from ml import create_summary

async def main():
    await client.start()

    result = {}
    
    for chanel in list_of_chanels:
        msgs_for_chanel = []
        async for message in client.iter_messages(chanel, limit=10):
            if is_today(message.date) and len(message.text) > 250:
                msgs_for_chanel.append(message.text)
        
        if msgs_for_chanel:
            result[chanel] = msgs_for_chanel
            
        print(f"for chanel {chanel} found {len(msgs_for_chanel)} messages")
    
    message_to_send = f"Summary for date {datetime.datetime.now().date()}"

    for chanel in result:
        summary = create_summary("new_msg:\n".join(result[chanel]), model_name)
        chanel_sum = f"\n\nSummary for chanel {chanel} :\n{summary}"
        print(chanel_sum)
        message_to_send += chanel_sum
        
    destination_user_username=config.get("send_to", "@astifer")
    entity = await client.get_entity(destination_user_username)
    await client.send_message(entity=entity, message=message_to_send)

load_dotenv()

api_token = os.getenv('API_TOKEN')
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

client = TelegramClient('session', api_id, api_hash)
list_of_chanels = get_list_of_chanels()
prefixes = get_prefix_for_chanels()

config = get_config()
model_name = config.get('model', 'local')


with client:
    client.loop.run_until_complete(main())


