from discord.ext import commands
import discord
import asyncio
import datetime
import os
import praw
from utils.constants import BLURPLE_COLOR

class API:
    """API Commands for the bot."""

    def __init__(self, bot):
        self.bot = bot
        self.reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                     user_agent=os.getenv('REDDIT_USER_AGENT'))

    def do_meme(self):
        memes_submissions = self.reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        return submission.url

    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.cooldown(1.0, 20.0, commands.BucketType.user)
    async def meme(self, ctx):
        """Generates a random meme from reddit."""
        async with ctx.typing():
            b = await self.bot.loop.run_in_executor(None, self.do_meme)
            embed = discord.Embed(color=BLURPLE_COLOR)
            embed.set_image(url=b)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(API(bot))
