import profanity_check
import re
import logging
import discord
import importlib
import sys
import json
import string
import random
from typing import *

debug = False
logger = logging.getLogger("logs")

# file
def loadfile(file: str):
    with open(file,"r") as file:
        return json.load(file)
        
def loadid(file, id):
    data = loadfile(file)
    return data[id]

def loadrecent(file):
    # TODO: find a way load the most recent
    return 0

def dumpfile(file, data):
    with open(file, "w") as file:
        json.dump(data, file, indent=4)

def dumpid(file, id, data):
    dat = loadfile(file, id)
    dat[id] = data
    dumpfile(file, dat)
        
def moddata(file, id, data):
    cont = loadid(file, id)
    cont[id] = data
    dumpfile(file, cont)

# app
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

def generateid(file, prefix=""):
    chars = string.ascii_uppercase, string.digits
    while True:
        random_id = prefix + ''.join(random.choices(chars, k=6))
        existing = loadid(file, "ids")
        if random_id not in existing:
            existing.add(random_id)
            dumpid(file, "ids", existing)
            return random_id
