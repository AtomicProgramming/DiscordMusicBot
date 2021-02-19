import discord
from discord.ext import commands

from logger import logger
from bot import config


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Successfully logged into discord as {}".format(self.client.user))
        await self.client.change_presence(activity=discord.Game("Listening to {}".format(config.get_prefix())))


def setup(client):
    client.add_cog(Events(client))

