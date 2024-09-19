import discord, datafun, genfun, os, logging
from dotenv import load_dotenv
import cogs.order as c 
import cogs.menu as m

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
bot = discord.Bot(intents=intents, debug_guilds=[1270760868321431622])

@bot.event
async def on_ready():
    logger.info("bot started!! :3")

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
cogs_list = [
    'account',
    'menu',
    'order',
    'admin'
]

loadedcogs = {}
logger.info(f"attempting to load cogs...")
for cog in cogs_list:
    try:
        logger.info(f"attempting to load cogs.{cog}...")
        bot.load_extension(f'cogs.{cog}')
        logger.info(f"loaded cogs.{cog}")
        loadedcogs[cog] = "true"
    except Exception as e:
        genfun.errormes(e)
        loadedcogs[cog] = "false"
logger.info(f"loadedcogs: {loadedcogs}")

@bot.slash_command(name="test")
async def test(ctx):
    await ctx.respond("bot is working!")
    


# starting the bot itself
bot.run(__TOKEN)
