# ©️biisal jai shree krishna 😎
from os import environ
from dotenv import load_dotenv

load_dotenv()

API_ID = environ.get("API_ID" , "23615625")
API_HASH = environ.get("API_HASH" , "6d3442904a75dd51ae064629248f3c9d")
BOT_TOKEN = environ.get("BOT_TOKEN" , "7980456184:AAHCdiFB3e9GMCiZdkl76g3aggx9dBCGaKY")
ADMIN = int(environ.get("ADMIN" , "7093899037"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1002150125584"))
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002304384234")
MONGO_URL = environ.get("MONGO_URL" , "mongodb+srv://userusa:userusa@shubhmoviebot.u0ngr.mongodb.net/?retryWrites=true&w=majority&appName=shubhmoviebot")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1002376520813")
)
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
