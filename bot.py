from discord.ext import commands
import discord
import asyncio
import datetime
import os

bot = commands.Bot(command_prefix=commands.when_mentioned_or('~~'), description="\uFEFF")
initial_extensions = ['cogs.owner','cogs.eh','cogs.misc','cogs.api']
BOT_LAUNCH_TIME = datetime.datetime.utcnow()

@bot.event
async def on_ready():
    print(f"{len(bot.users)} users.")
    print(f"I'm connected on {bot.user.name} with the ID {bot.user.id}.")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"~~help"))

@bot.command()
async def uptime(ctx):
        delta_uptime = datetime.datetime.utcnow() - BOT_LAUNCH_TIME
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")	
	
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(os.getenv('BOT_TOKEN'))

