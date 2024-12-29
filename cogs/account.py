import main, os, discord, datafun, logging
from discord.ext import commands
from typing import Any

logger = logging.getLogger("logs")

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

USERPATH = "appdata/user/users.json"

class Account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    account = discord.SlashCommandGroup("account", "commands related to accounts")
    
    

def setup(bot):
    bot.add_cog(Account(bot))