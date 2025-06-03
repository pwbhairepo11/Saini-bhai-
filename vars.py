#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "28460032"))
API_HASH = environ.get("API_HASH", "1457c3ba64719a1e442aae67217b67c2")
BOT_TOKEN = environ.get("BOT_TOKEN", "8179018409:AAFJXakzOiUGV2QNBg-ZfmAAWShJhC2ifc4")
OWNER = int(environ.get("OWNER", "6977768796"))
CREDIT = "💚 कुंतल जी 💚"
AUTH_USER = os.environ.get('AUTH_USERS', '6977768796').split(',')
AUTH_USERS = [int(user_id) for user_id in 6977768796]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
