from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "14447155"))
API_HASH = getenv("API_HASH","ef370b85866716be28c348f5f96db1e4")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN","5536017329:AAGccrIGEo95SLLa19fYfrxNmB0DfIcWQdk")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
LOGGER_ID = int(getenv("LOGGER_ID","-1001584910654"))
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5442143084").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/74fb72c6e6b04b6fc5eef.jpg")
START_IMG = getenv("START_IMG","https://te.legra.ph/file/ec2b6bf8d17962430bc7e.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TeamTrickyYash")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/TrickyYash")

STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1574818111").split()))
