import discord, datafun


print("init sequence beginning")
client = datafun.fetchdatabyid("dat.json", "client")
manager = datafun.fetchdatabyid("dat.json", "manager")
log = datafun.fetchdatabyid("dat.json", "log")
settings = datafun.fetchdatabyid("dat.json", "dev")
guild = datafun.fetchdatabyid("dat.json", "guild")


# bot yay
client = discord.Bot()

async def comingsoon(ctx):
    await ctx.respond("coming soon!")


@client.slash_command(name="test", guild_id=guild)
async def test(ctx):
    await ctx.respond("slash commands working!")

@client.slash_command(name="order", guild_id=guild)
async def order(ctx):
    comingsoon()

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
