# cogs/admin.py

import discord, importlib, logging, sys
from discord.ext import commands
from main import coglist, modulelist


logger = logging.getLogger("logs")

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="reloadmodule")
    async def reloadmodule(self, ctx, module: discord.Option(str, choices=modulelist)): # type: ignore
        try:
            importlib.reload(module)
            await ctx.send(f"{module} reloaded")
            logger.info("reloaded main event handlers")
        except Exception as e:
            await ctx.send(f"Error reloading: {e}")
            logger.error("event handlers could not be reloaded")
            logger.error(e)
            
    @commands.command(name="reloadallmodules")
    async def reloadallmodules(self, ctx):
        modules = list(sys.modules.keys())
        loadedmodules = {}
        logger.info(f"loading modules...")
        for module in modules:
            if module in ('__main__', "builtins") or module.startswith("_"):
                continue

            try:
                logger.info(f"    loading {module}...")
                importlib.reload(sys.modules[module])
                logger.info(f"loaded {module}")
                loadedmodules[module] = "true"
                logger.info(f"    loading {module}...done")
            except Exception as e:
                logger.warning(f" loading {module}...failed")
                logger.warning(f"error: {e}")
                loadedmodules[module] = "false"
        logger.info(f"loading modules...done") 

    @commands.command(name='reloadcog')
    async def reload_cog(self, ctx, cog: discord.Option(str, choices=coglist)): # type: ignore
        try:
            self.bot.reload_extension(f'cogs.{cog}')
            await ctx.send(f"Reloaded {cog} cog.")
        except Exception as e:
            await ctx.send(f"Failed to reload {cog} cog: {e}")

# Required setup function for cog loading
def setup(bot):
    bot.add_cog(Admin(bot))