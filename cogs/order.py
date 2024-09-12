import main, os, discord, datafun
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
print("fetching values...")
MANAGER = os.getenv("MANAGER")
CLIENT = os.getenv("CLIENT")
print("done.")
PATH = "./appdata/order/"
USERDATAPATH = "./appdata/user"

class Order(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    order = discord.SlashCommandGroup("order", "commands related to ordering")
    
    @order.command(name="start")
    async def startorder(self, ctx):
        orderid = int(datafun.fetchdata(PATH))+1
        await ctx.respond(f"order id: {orderid}")
    
        
def setup(bot):
    bot.add_cog(Order(bot))