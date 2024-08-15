import discord, datafun
import cogs.client as c 
import cogs.manager as m


print("init sequence beginning")
client = int(datafun.fetchdatabyid("channels.json", "client"))
manager = int(datafun.fetchdatabyid("channels.json", "manager"))
log = int(datafun.fetchdatabyid("channels.json", "log"))
settings = int(datafun.fetchdatabyid("channels.json", "dev"))
guild = int(datafun.fetchdatabyid("channels.json", "guild"))
log = int(datafun.fetchdatabyid("channels.json", "log"))

# starting bot
client = discord.Bot()
log.message.send("bot starting...")

# loading cogs
cogs_list = [
    'client',
    'manager'
] 

for cog in cogs_list:
    try:
        log.message.send("attempting to load cogs.{cog}...")
        client.load_extension(f'cogs.{cog}')
        log.message.send("loaded cogs.{cog}")
    except Exception as e:
        log.message.send("ERROR??!?!?!?!?!??? output:\n{e}\nend of output... aw :(")
log.message.send("loaded all cogs")

async def comingsoon(ctx):
    await ctx.respond("coming soon!")
    
@client.event
async def on_ready():
    log.message.send("init sequence successful!! :3")
    
load = discord.SlashCommandGroup("load", "admin command for loading cogs")
unload = load.create_subgroup("unload", "admin command for unloading cogs")

@load.command()
async def manager(ctx):
    try:
        log.message.send("attempting to load cogs.manager...")
        client.load_extension(f'cogs.manager')
        log.message.send("loaded cogs.manager")
    except Exception as e:
        log.message.send("ERROR??!?!?!?!?!??? output:\n{e}\nend of output... aw :(")
    
@load.command()
async def client(ctx):
    try:
        log.message.send("attempting to load cogs.client...")
        client.load_extension(f'cogs.client')
        log.message.send("loaded cogs.client")
    except Exception as e:
        log.message.send("ERROR??!?!?!?!?!??? output:\n{e}\nend of output... aw :(")
    
@unload.command()
async def manager(ctx):
    try:
        log.message.send("attempting to unload cogs.manager...")
        client.unload_extension(f'cogs.manager')
        log.message.send("unloaded cogs.manager")
    except Exception as e:
        log.message.send("ERROR??!?!?!?!?!??? output:\n{e}\nend of output... aw :(")

@unload.command()
async def client(ctx):
    try:
        log.message.send("attempting to unload cogs.client...")
        client.unload_extension(f'cogs.client')
        log.message.send("unloaded cogs.client")
    except Exception as e:
        log.message.send("ERROR??!?!?!?!?!??? output:\n{e}\nend of output... aw :(")

@client.slash_command(name="test", guild_id=guild)
async def test(ctx):
    await ctx.respond("slash commands working!")

@client.slash_command(name="order", guild_id=guild)
async def order(ctx):
    comingsoon()



# starting the bot itself
client.run(datafun.fetchdatabyid("dat.json", "token"))
