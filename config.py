import os
from telethon import TelegramClient
api_id = 22437328
api_hash = "2f51bbe49cf796d04086ad882236a9db"
bot_token = "6533903254:AAE-GdhuAHQZ0ihO2MB2_e694seEjDgMqzw"
skeleton_url = "https://play.google.com/store/apps/details?id=com.utkarshnew.android"

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
skeleton_url = os.environ.get('SKELETON_URL')


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


