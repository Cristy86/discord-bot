from utils.constants import SUCCESS_EMOJI, WRONG_EMOJI, LOADING_EMOJI
from discord.ext import commands
import asyncio
import traceback
import discord
import datetime
BOT_LAUNCH_TIME = datetime.datetime.utcnow()

class Misc:
    """Misc commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uptime(self, ctx):
        delta_uptime = datetime.datetime.utcnow() - BOT_LAUNCH_TIME
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")

def setup(bot):
    bot.add_cog(Misc(bot))
