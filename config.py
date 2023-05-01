import os
from telethon import TelegramClient
api_id = 22274213
api_hash = "53db38b5012cc9323a39c72b266855d3"
bot_token = "5732523875:AAHZpUx0kXy5jcxIFA5Gj3g3CLTQFdJfSRw"
skeleton_url = ""

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
skeleton_url = os.environ.get('SKELETON_URL')


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


