import discord, datafun
import cogs.client as c 
import cogs.manager as m


# starting bot
intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

print("init sequence beginning")
client = int(datafun.fetchdatabyid("channels.json", "client"))
manager = int(datafun.fetchdatabyid("channels.json", "manager"))
settings = int(datafun.fetchdatabyid("channels.json", "dev"))

# loading cogs
cogs_list = [
    'client',
    'manager'
] 

for cog in cogs_list:
    try:
        print(f"attempting to load cogs.{cog}...")
        bot.load_extension(f'cogs.{cog}')
        print(f"loaded cogs.{cog}")
    except Exception as e:
        print(f"ERROR??!?!?!?!?!??? output:\n{e}\nend of output... aw :(")
print("loaded all cogs")

async def comingsoon(ctx):
    await ctx.respond("coming soon!")
    
@bot.event
async def on_ready():
    print("bot is ready!! :3")
    

@bot.slash_command(name="test")
async def test(ctx):
    await ctx.respond("bot is working!")

@bot.slash_command(name="order")
async def order(ctx):
    comingsoon()
    
load = discord.SlashCommandGroup("load", "admin command for loading cogs")
unload = load.create_subgroup("unload", "admin command for unloading cogs")

@load.command()
async def manager(ctx):
    try:
        print("attempting to load cogs.manager...")
        bot.load_extension(f'cogs.manager')
        print("loaded cogs.manager")
    except Exception as e:
        print(f"ERROR??!?!?!?!?!??? output:\n{e}\nend of output... aw :(")
    
@load.command()
async def client(ctx):
    try:
        ctx.response("attempting to load cogs.client...")
        bot.load_extension(f'cogs.client')
        ctx.response("loaded cogs.client")
    except Exception as e:
        print(f"ERROR??!?!?!?!?!??? output:\n{e}\nend of output... aw :(")
    
@unload.command()
async def manager(ctx):
    try:
        ctx.response("attempting to unload cogs.manager...")
        bot.unload_extension(f'cogs.manager')
        ctx.response("unloaded cogs.manager")
    except Exception as e:
        print(f"ERROR??!?!?!?!?!??? output:\n{e}\nend of output... aw :(")

@unload.command()
async def client(ctx):
    try:
        ctx.response("attempting to unload cogs.client...")
        bot.unload_extension(f'cogs.client')
        ctx.response("unloaded cogs.client")
    except Exception as e:
        print(f"ERROR??!?!?!?!?!??? output:\n{e}\nend of output... aw :(")

# starting the bot itself
bot.run(datafun.fetchdatabyid("dat.json", "token"))
