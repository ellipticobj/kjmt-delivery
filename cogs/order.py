import main, os, discord, utils
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
print("fetching values...")
MANAGER = os.getenv("MANAGER")
CLIENT = os.getenv("CLIENT")
print("done.")
file = "./appdata/orders.json"

class OrderIdemDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="item + price", description="description")
        ]
        super().__init__(placeholder="choose your item...", min_values=1, options=options)
    
    async def callback(self, interaction: discord.Interaction):
        # TODO: do actual stuff here
        await interaction.response.send_message(f"You selected: {self.values[0]}", ephemeral=True)

class OrderForm(discord.ui.modal):
    def __init__(self):
        super().__init__(title="Your order")
    
    self.add_item(discord.ui.InputText(label=""))

class Order(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    order = discord.SlashCommandGroup("order", "commands related to ordering")
    
    @order.command(name="start")
    async def startorder(self, ctx):
        uniqueid = utils.generateid(file, "order_")
        ctx.respond(f"order started with id {uniqueid}.", ephemeral=True)
        
        


def setup(bot):
    bot.add_cog(Order(bot))