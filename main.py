import discord, os, logging, inspect
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

modulelist = [name for name, obj in inspect.getmembers(genfun, inspect.isfunction)]

loadedcogs = genfun.loadcogs(coglist, client)
logger.info(f"loaded cogs: {loadedcogs}")

@client.event
async def on_ready():
    logger.info("bot started!! :3")

@client.slash_command(name="test")
async def test(ctx):
    await ctx.respond("bot is working!")
    


# starting the bot itself
client.run(__TOKEN)
