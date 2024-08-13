import pycord, datafun

# setting discord bot intents (perms)
intents = pycord.Intents.default()
intents.message_content = True


client = datafun.fetchdatabyid("dat.json", "client")
manager = datafun.fetchdatabyid("dat.json", "manager")
log = datafun.fetchdatabyid("dat.json", "log")
settings = datafun.fetchdatabyid("dat.json", "dev")

# bot yay
client = pycord.ext.commands.Bot()

@client.slash_command(
    name="test",
    guild_id=datafun.fetchdatabyid("dat.json", "guild")
)

async def test(ctx):
    await ctx.respond("slash commands working!")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# starting the bot itself
client.run(datafun.fetchdatabyid("dat.json", "token"))
