import main, os
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
        
    @commands.group()
    async def menu(ctx):
        if ctx.channel.id == MANAGER:
            # PLANNED show ui to edit menu
            # TODO for now, just read menu and show it in a card
            pass
        elif ctx.channel.id == CLIENT:
            # TODO read menu and show it in a card
            pass
        
def setup(bot):
    bot.add_cog(Manager(bot))