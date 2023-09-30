from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "12706503")
APP_HASH = os.environ.get("APP_HASH", "4344a75f9ae9d1d03f577b61e7313884")
SESSION = os.environ.get("SESSION")
ha313so = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
ha313so.start()
