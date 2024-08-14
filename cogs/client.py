import discord
from discord.ext import commands

class Client(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        