import requests
import logging

logging.basicConfig(filename='pokeroll.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')
MESSAGE = '$p'

headers = {
    'Authorization': TOKEN,
    'Content-Type': 'application/json',
}

data = {
    'content': MESSAGE,
}

try:
    response = requests.post(f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages', headers=headers, json=data)
    
    logging.debug(f'Response status code: {response.status_code}')
    logging.debug(f'Response text: {response.text}')
    
    if response.status_code == 200:
        logging.info('Message sent successfully')
    else:
        logging.error(f'Failed to send message: {response.status_code}')

except Exception as e:
    logging.error(f'An error occurred: {e}')