import discord, os, logging, inspect, importlib
import datafun, genfun
from datafun import *
from genfun import *
from dotenv import load_dotenv

logger = logging.getLogger("logs")
logger.setLevel(logging.INFO)
consolehandler = logging.StreamHandler()
filehandler = logging.FileHandler("./main.log")
consolehandler.setLevel(logging.INFO)
filehandler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - [%(levelname)s]: %(message)s")
consolehandler.setFormatter(formatter)
filehandler.setFormatter(formatter)
logger.addHandler(consolehandler)
logger.addHandler(filehandler)

# starting bot
intents = discord.Intents.all()
client = discord.Bot(intents=intents, debug_guilds=[1270760868321431622])

logger.info("init sequence beginning")
logger.info("loading dotenv...")
load_dotenv()
logger.info("loading dotenv...done")
logger.info("fetching values...")
__TOKEN = os.getenv("TOKEN")
CLIENT = os.getenv("CLIENT")
MANAGER = os.getenv("MANAGER")
logger.info("fetching values...done")

# loading cogs
coglist = [
    'account',
    'menu',
    'order',
    'admin'
]

modulelist = [name for name, _ in inspect.getmembers(genfun, inspect.isfunction)] 
modulelist += [name for name, _ in inspect.getmembers(datafun, inspect.isfunction)]

for module in modulelist:
    importlib.import_module(module)

loadedcogs = loadcogs(coglist, client)
logger.info(f"loaded cogs: {loadedcogs}")

loadedmodules = loadmodules(modulelist)
logger.info(f"loaded modules: {loadedmodules}")

@client.event
async def on_ready():
    logger.info(f"signed in as {client.user}")
    logger.info("bot started!! :3")


# starting the bot itself
client.run(__TOKEN)
