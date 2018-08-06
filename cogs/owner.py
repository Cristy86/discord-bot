from utils.constants import SUCCESS_EMOJI, WRONG_EMOJI, LOADING_EMOJI
from discord.ext import commands
import asyncio
import traceback
import discord
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import copy
from typing import Union
import datetime
from collections import Counter

class Owner:
    """Owner commands."""

    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    async def __local_check(self, ctx):
        return await self.bot.is_owner(ctx.author)

    @commands.command(pass_context=True, hidden=False, name='eval')
    async def _eval(self, ctx, *, body: str):
        """Evaluates code."""

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'
        await ctx.message.add_reaction(LOADING_EMOJI)

        try:
            exec(to_compile, env)
        except Exception as e:
            await ctx.message.remove_reaction(LOADING_EMOJI, member=ctx.me)
            await ctx.message.add_reaction(WRONG_EMOJI)
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.message.remove_reaction(LOADING_EMOJI, member=ctx.me)
            await ctx.message.add_reaction(WRONG_EMOJI)
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.remove_reaction(LOADING_EMOJI, member=ctx.me)
                await ctx.message.add_reaction(SUCCESS_EMOJI)
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')

    @commands.command(name="die")
    async def _logout(self, ctx):
        """Makes the bot to die."""
        await ctx.send(f"<{SUCCESS_EMOJI}> **`Goodbye.`**")
        await self.bot.logout()


def setup(bot):
    bot.add_cog(Owner(bot))
