import main, os, discord, datafun
from discord.ext import commands
from dotenv import load_dotenv

class Account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    defaultvals = {
            "username": "Anon",
            "displayname": "Anon",
            "deliveryperson": False,
            "orders": [],
            "cards": [],
            "addresses": [],
            "loyalty": [],
            "banned": False,
            "staff": False,
            "password": "d919a100ce6b45524d415d52d088d5817587c6dd8c3691b03b8063c44d043523"
        }
        
    account = discord.SlashCommandGroup("account", "commands related to accounts")
    
    @account.command(name="create", username="Anon", displayname="Anon")
    async def createacc(self, ctx):
        await ctx.response(f"Account creation in progress...")
        
        

def setup(bot):
    bot.add_cog(Account(bot))