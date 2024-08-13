import discord, datafun

# setting discord bot intents (perms)
intents = discord.Intents.default()
intents.message_content = True


client = datafun.fetchdatabyid("dat.json", "client")
manager = datafun.fetchdatabyid("dat.json", "manager")
log = datafun.fetchdatabyid("dat.json", "log")
settings = datafun.fetchdatabyid("dat.json", "dev")

# bot yay
client = discord.Client(intents=intents)


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
