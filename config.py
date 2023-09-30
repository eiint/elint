from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "23448442")
APP_HASH = os.environ.get("APP_HASH", "c866f6a9330db54550db52c2c590d87c")
SESSION = os.environ.get("SESSION")
sajad = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
sajad.start()
