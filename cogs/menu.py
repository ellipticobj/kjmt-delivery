import main, os, discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
print("fetching values...")
MANAGER = os.getenv("MANAGER")
CLIENT = os.getenv("CLIENT")
print("done.")

class Manager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        
def setup(bot):
    bot.add_cog(Manager(bot))