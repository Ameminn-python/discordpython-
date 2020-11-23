import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='/')
Token = "" #BotアカウントのTokenを代入


bot.load_extension('eval')

bot.run(Token)
