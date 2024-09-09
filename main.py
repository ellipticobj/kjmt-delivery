import discord, datafun, genfun, os
from dotenv import load_dotenv
import cogs.client as c 
import cogs.menu as m

# starting bot
intents = discord.Intents.all()
bot = discord.Bot(intents=intents, debug_guilds=[1270760868321431622])

@bot.event
async def on_ready():
    print("bot started!! :3")
    log = bot.get_channel(1271400775611846656)
    await log.send("test message")

print("init sequence beginning")
print("loading dotenv...")
load_dotenv()
print("fetching values...")
__TOKEN = os.getenv("TOKEN")
client = os.getenv("CLIENT")
manager = os.getenv("MANAGER")
settings = os.getenv("DEV")
print("done")

# loading cogs
cogs_list = [
    'client',
    'manager'
]

loadedcogs = {}
print(f"attempting to load cogs...")
for cog in cogs_list:
    try:
        print(f"attempting to load cogs.{cog}...")
        bot.load_extension(f'cogs.{cog}')
        print(f"loaded cogs.{cog}")
        loadedcogs[cog] = "true"
    except Exception as e:
        genfun.errormes(e)
        loadedcogs[cog] = "false"
print(f"loadedcogs: {loadedcogs}")
    
async def comingsoon(ctx):
    await ctx.respond("coming soon!")

@bot.slash_command(name="test")
async def test(ctx):
    await ctx.respond("bot is working!")

@bot.slash_command(name="order")
async def order(ctx):
    comingsoon()
    
loadcog = discord.SlashCommandGroup("loadcog", "admin command for loading cogs")
unloadcog = discord.SlashCommandGroup("unloadcog", "admin command for unloading cogs")

@loadcog.command()
async def manager(ctx):
    bot.load_extension('cogs.manager')
    
# @loadcog.command()
# async def client(ctx):
#     try:
#         print("attempting to load cogs.client...")
#         bot.load_extension(f'cogs.client')
#         print("loaded cogs.client")
#     except Exception as e:
#         genfun.errormes(e)
    
# @unloadcog.command()
# async def manager(ctx):
#     try:
#         print("attempting to unload cogs.manager...")
#         bot.unload_extension(f'cogs.manager')
#         print("unloaded cogs.manager")
#     except Exception as e:
#         genfun.errormes(e)

# @unloadcog.command()
# async def client(ctx):
#     try:
#         print("attempting to unload cogs.client...")
#         bot.unload_extension(f'cogs.client')
#         print("unloaded cogs.client")
#     except Exception as e:
#         genfun.errormes(e)

# starting the bot itself
bot.add_application_command(loadcog)
bot.add_application_command(unloadcog)
bot.run(__TOKEN)
