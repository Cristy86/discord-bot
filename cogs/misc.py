from utils.constants import SUCCESS_EMOJI, WRONG_EMOJI, LOADING_EMOJI
from discord.ext import commands
import asyncio
import traceback
import discord
import datetime, random

class Misc:
    """Misc commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball")
    async def _ball(self, ctx, *, question:str):
        """A usual 8ball..."""

        if ctx.author.bot:
            return
        
        results = ["It is certain"," It is decidedly so","Without a doubt","Yes, definitely","You may rely on it","As I see it, yes"," Most likely","Outlook good","Yes","Signs point to yes"," Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
        await ctx.send(f"The 🎱 says: **`{random.choice(results)}.`**")

def setup(bot):
    bot.add_cog(Misc(bot))
