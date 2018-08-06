import traceback
import sys
from discord.ext import commands
import discord
from datetime import datetime
from utils.constants import WRONG_EMOJI

class CommandErrorHandler:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.MissingRequiredArgument, commands.BadArgument, commands.NoPrivateMessage, commands.CheckFailure, commands.DisabledCommand, commands.CommandInvokeError, commands.TooManyArguments, commands.UserInputError, commands.NotOwner, commands.MissingPermissions, commands.BotMissingPermissions, AttributeError, KeyError, TypeError, ValueError, discord.Forbidden, discord.ConnectionClosed, discord.HTTPException, UnboundLocalError, NameError, FileNotFoundError, RuntimeError, RuntimeWarning, OSError, IndexError, ZeroDivisionError, discord.ClientException)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            await ctx.send(f"<{WRONG_EMOJI}> **`{error}`**")


        elif isinstance(error, commands.CommandOnCooldown):
            if await self.bot.is_owner(ctx.author):
                await ctx.reinvoke()
            else:
                await ctx.send(f"<{WRONG_EMOJI}> **`{error}`**")

        elif isinstance(error, commands.DisabledCommand):
            if await self.bot.is_owner(ctx.author):
                await ctx.reinvoke()
            else:
                await ctx.send(f"<{WRONG_EMOJI}> **`{error}`**")

        elif isinstance(error, commands.CommandNotFound):
            return


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
