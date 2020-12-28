import discord
from discord.ext import commands
import json

bot=commands.Bot(command_prefix='/')
Token = "" #BotアカウントのTokenを代入


@bot.event
async def on_command_error(ctx, error):
    official_server = bot.get_guild() #guild_idをセット
    error_ch = official_server.get_channel()#チャンネル idをセット
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send('cause error')
    try:
        await error_ch.send(error_msg)
    except:
        with open(r'error.log',mode='a') as f:
            f.write('\n-------\n'+errormsg+'\n-------\n')
        await ctx.send('エラー処理の段階でエラーが発生したのでログに記録しました。')
    else:
        pass

@bot.command()
async def load(ctx,module:str):
    bot.load_extension(module)
    await ctx.send('succsess')
   
@bot.command()
async def reload(ctx,md):
    """Cogファイルをリロードします。"""
    bot.reload_extension(md)
    await ctx.send('succsess')
    
    
@bot.command()
async def unload(ctx,module:str):
    try:
        bot.unload_extension(module)
    except Extension as e:
        await ctx.message.add_reaction('\U0001f196')  #Unicode 後から追加
        message = f'```\n{e}\n```'
        await ctx.send(message)
    else:
        awiat ctx.send('Cogのアンロードに成功しました。')

    

bot.load_extension('eval')

bot.run(Token)
