import datafun, profanity_check, re, logging, discord
from typing import Tuple

logger = logging.getLogger("logs")

def usrnameisvalid(username: str) -> Tuple[bool, str]:
    '''
    checks for validity of username
    '''
    if profanity_check.predict([username]):
        return False, "Username may contain offensive terms."
    if len(username) < 2 or len(username) > 24:
        return False, "Username must be between 2 and 24 characters"
    if not re.match(r'^\w+$', username):
        return False, "Username can only contain letters, numbers or underscores"
    return True, ""

def loadcogs(coglist: list[str], client: discord.Bot) -> dict[str,str]:
    loadedcogs = {}
    logger.info(f"loading cogs...")
    for cog in coglist:
        try:
            logger.info(f"    loading cogs.{cog}...")
            client.load_extension(f'cogs.{cog}')
            logger.info(f"loaded cogs.{cog}")
            loadedcogs[cog] = "true"
            logger.info(f"    loading cogs.{cog}...done")
        except Exception as e:
            logger.warning(f" loading cogs.{cog}...failed")
            logger.warning(f"error: {e}")
            loadedcogs[cog] = "false"
    logger.info(f"loading cogs...done")   
    return loadedcogs