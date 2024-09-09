import discord
from discord.ext import commands

class Client(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    delivery = discord.SlashCommandGroup("delivery", "functions related to delivering")
    order = discord.SlashCommandGroup("order", "functions related to ordering")
    account = discord.SlashCommandGroup("account", "functions related to accounts")
    
        
def setup(bot):
    bot.add_cog(Client(bot))
    