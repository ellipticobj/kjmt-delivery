import discord, datafun, genfun, os
from dotenv import load_dotenv
import cogs.order as c 
import cogs.menu as m

# starting bot
intents = discord.Intents.all()
bot = discord.Bot(intents=intents, debug_guilds=[1270760868321431622])

@bot.event
async def on_ready():
    print("bot started!! :3")

print("init sequence beginning")
print("loading dotenv...")
load_dotenv()
print("fetching values...")
__TOKEN = os.getenv("TOKEN")
CLIENT = os.getenv("CLIENT")
MANAGER = os.getenv("MANAGER")
SETTINGS = os.getenv("DEV")
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
    await comingsoon(ctx)
    
loadcog = discord.SlashCommandGroup("loadcog", "admin command for loading cogs")
unloadcog = discord.SlashCommandGroup("unloadcog", "admin command for unloading cogs")

@loadcog.command(name="manager")
async def loadmanager(ctx):
    if not loadedcogs["manager"] == 'false':
        try:
            bot.load_extension('cogs.manager')
            await ctx.respond("cogs.manager loaded successfully")
            loadedcogs["manager"] = True
        except Exception as e:
            await ctx.respond("cogs.manager failed to load :(")
            await ctx.respond(f"error: {e}", ephemeral=True)
    else:
        await ctx.respond("cogs.manager is already loaded")

@loadcog.command(name="client")
async def loadclient(ctx):
    if loadedcogs["client"] == 'false':
        try:
            bot.load_extension('cogs.client')
            await ctx.respond("cogs.client loaded successfully")
        except Exception as e:
            await ctx.respond("cogs.client failed to load :(")
            await ctx.respond(f"error: {e}", ephemeral=True)
    else:
        await ctx.respond("cogs.client is already loaded")
    
@unloadcog.command(name="manager")
async def unloadmanager(ctx):
    try:
        print("attempting to unload cogs.manager...")
        bot.unload_extension(f'cogs.manager')
        print("unloaded cogs.manager")
    except Exception as e:
        await ctx.respond("cogs.manager couldnt unload :(")
        await ctx.respond(f"error: {e}", ephemeral=True)

@unloadcog.command(name="client")
async def unloadclient(ctx):
    try:
        await ctx.respond("attempting to unload cogs.client...", ephemeral=True)
        bot.unload_extension(f'cogs.client')
        await ctx.respond("unloaded cogs.client")
    except Exception as e:
        await ctx.respond("cogs.client couldnt unload :(")
        await ctx.respond(f"error: {e}", ephemeral=True)

# starting the bot itself
bot.add_application_command(loadcog)
bot.add_application_command(unloadcog)
bot.run(__TOKEN)
