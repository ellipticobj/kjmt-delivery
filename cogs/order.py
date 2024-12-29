import main, os, discord, utils
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
print("fetching values...")
MANAGER = os.getenv("MANAGER")
CLIENT = os.getenv("CLIENT")
print("done.")
PATH = "./appdata/orders.json"

class Order(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    order = discord.SlashCommandGroup("order", "commands related to ordering")
    
    @order.command(name="start")
    async def startorder(self, ctx):
        return 0
    
        
def setup(bot):
    bot.add_cog(Order(bot))