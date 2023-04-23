import discord
from discord.ext import commands
from cog import config
import asyncio
from discord import FFmpegPCMAudio
from cog import thecog
import random

class bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix= commands.when_mentioned_or("?"),
            intents=discord.Intents.all(),
            help_command =  commands.DefaultHelpCommand(
            no_category = None
)
        )
    async def on_ready(self):
        print(self.user)
        await bot.tree.sync()
    async def setup_hook(self):
        await bot.load_extension("cog.thecog")
    
bot = bot()
bot.run(config.BOT_TOKEN, reconnect=True)
    