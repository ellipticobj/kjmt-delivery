import discord, datafun
import cogs.client as c 
import cogs.manager as m


print("init sequence beginning")
client = int(datafun.fetchdatabyid("dat.json", "client"))
manager = int(datafun.fetchdatabyid("dat.json", "manager"))
log = int(datafun.fetchdatabyid("dat.json", "log"))
settings = int(datafun.fetchdatabyid("dat.json", "dev"))
guild = int(datafun.fetchdatabyid("dat.json", "guild"))
log = int(datafun.fetchdatabyid("dat.json", "log"))

# starting bot
client = discord.Bot()
log.send("bot starting...")

# loading cogs
cogs_list = [
    'client',
    'manager'
] 

for cog in cogs_list:
    try:
        client.load_extension(f'cogs.{cog}')
    except Exception as e:
        log.send("ERROR??!?!?!?!?!??? output:\n{e}\nend of output... aw :(")
    log.send("loaded cogs.{cog}")
log.send("loaded all cogs")

async def comingsoon(ctx):
    await ctx.respond("coming soon!")
    
@client.event
async def on_ready():
    log.send("init sequence successful!! :3")

@client.slash_command(name="test", guild_id=guild)
async def test(ctx):
    await ctx.respond("slash commands working!")

@client.slash_command(name="order", guild_id=guild)
async def order(ctx):
    comingsoon()



# starting the bot itself
client.run(datafun.fetchdatabyid("dat.json", "token"))
