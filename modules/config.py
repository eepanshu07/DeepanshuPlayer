import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "17438949"))
API_HASH = getenv("API_HASH", "798f3353789b839736172578350b4bd4)
BOT_USERNAME = getenv("BOT_USERNAME", "Deep_VcMusic_Bot")
BOT_TOKEN = getenv("BOT_TOKEN", "5421935228:AAHI5MYitIV17icoWR5FYGq5zk8hWfctZcc")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQA0lQXy567euvw98qyoQMdU-FQ2QOkhkw5tIrbbYsmtjUOzVxzW3s0oPiyTJ6XNQe1tfW5pIPxJGJwGbM-M4bYmEGePY11_PYyfwtHFfMH_rams5QKxK1ox0MZAalEFE7akr8a3XHlDPyV1vygU7Q4fV0kIMz3ga1gm1WsF6JVZU-2okEGL4835aiiOsFV7_Uw7qnwG1jyzc9eubpAzyY7Y-mJ_IEwcAmQDsKWxtXTH1ANjlNTN1oq3TdA79ySe2qelWPPVWl8qdrAu-AqJq57e8RgI4G3abS9iWwyaYtn5DI0DeiBkkcrgF2-_ekV7NIHYBLBC5qA-Q1xVj0MvNLT_WwsthAAyKqMTgHQAdv-PZHOlbKVKXsr2T7TBRy_pB2oxnuXKbV5oieqjC_-60jW0LuAC4QZ9Pn9HvSjjE2tRgWbpecKngvS55YSzpF6UzlykLIvlv0709nAqKhqQh9FOXYGaGID3WogRKniMidcsStvscZ_TRlwtEv4caMV9VjKLA7xTWNr4t2rss6AAAAASwVnR4A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1527459204 5346953228 5058237367 702821224 5168642497").split()))
aiohttpsession = aiohttp.ClientSession()
