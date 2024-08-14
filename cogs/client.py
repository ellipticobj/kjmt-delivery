import discord

class Client(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        