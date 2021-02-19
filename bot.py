import discord
from discord.ext import commands
from logger import logger
import json
import os


class Config:

    def __init__(self):
        with open("./data/config.json", "r") as f:
            self.config = json.load(f)

    def get_token(self):
        try:
            token = self.config['token']
            return token
        except KeyError:
            logger.fatal("Could not find discord token")
            exit(1)

    def get_prefix(self):
        try:
            token = self.config['prefix']
            return token
        except KeyError:
            logger.fatal("Could not find command prefix")
            exit(1)


def start_check():

    if not os.path.exists("./data"):
        os.mkdir("./data")

    if not os.path.exists("./data/config.json"):
        with open("./data/config.json", "w") as f:
            f.write("{}")
            f.close()


start_check()
config = Config()
client = commands.Bot(command_prefix=config.get_prefix())
start_check()
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        client.load_extension("cogs.{}".format(file[:-3]))
        logger.info("Successfully loaded {} cog".format(file[:-3]))
try:
    client.run(config.get_token())
except discord.errors.LoginFailure:
    logger.fatal("Failed to login to discord!")
