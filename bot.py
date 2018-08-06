
from discord.ext import commands
import discord
import asyncio
import datetime
import os

bot = commands.Bot(command_prefix=commands.when_mentioned_or('~~'), description="\uFEFF")
initial_extensions = ['cogs.owner','cogs.eh','cogs.misc']

@bot.event
async def on_ready():
    print(f"{len(bot.users)} users.")
    print(f"I'm connected on {bot.user.name} with the ID {bot.user.id}.")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"~~help"))

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(os.getenv('BOT_TOKEN'))

