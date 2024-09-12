import main, os, discord, datafun
from discord.ext import commands
from dotenv import load_dotenv

class Account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    account = discord.SlashCommandGroup("account", "commands related to accounts")
    
    @account.command(name="create")
    async def createacc(self, ctx):
        await ctx.response(f"Account creation in progress...")
        
        

def setup(bot):
    bot.add_cog(Account(bot))