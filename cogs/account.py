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
    
    
    @account.command(name="create")
    async def createacc(self, ctx, password, username="Anon", displayname="Anon"):
        uservals = defaultvals
        uservals["username"] = username
        uservals["displayname"] = displayname
        uservals["password"] = hash(password)
        uid = int(datafun.loaddata(USERPATH, findrecent=True))+1
        datafun.moddata(USERPATH, uid, uservals)
        await ctx.respond(f"account created with userid {uid}")
        
    @account.command(name="display", aliases=["show"])
    async def displayaccdetails(self, ctx):
        pass
    
    edit = account.subgroup("edit", "lets you edit your account")
    
    @edit.command(name="username")
    async def editusername(self, ctx, username: str):
        data: dict[str, dict[str, Any]] = datafun.__loaddata(USERPATH)
        logger.info(f"{ctx.author} is trying to change their username to ")
        for _, udata in data.items():
            if udata["username"] == username:
                await ctx.respond(f"This username is taken. Please choose another one.", ephemeral=True)
            
        

def setup(bot):
    bot.add_cog(Account(bot))