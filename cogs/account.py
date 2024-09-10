import main, os, discord, datafun
from discord.ext import commands
from dotenv import load_dotenv

class Account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

def setup(bot):
    bot.add_cog(Account(bot))