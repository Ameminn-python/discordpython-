import discord
from discord.ext import commands

class Sender(commands.Cog):
  
  def __init__(self,bot):
    self.bot =bot

  
  @commands.command()
  async def url(self,ctx,mid:int,cid:int=ctx.channel.id):
    try:
      g = ctx.guild
      ch = bot.get_channel(cid)
      msg = ch.fetch_messsage(mid)
    except:
      await ctx.send('メッセージ取得に失敗')
    else:
      atc_list = msg.attachments
      if atc_list != None:
        await ctx.send('ファイルが存在しません。')
      elif len(atc_list) >= 2:
        await ctx.send('ファイルが二つ以上添付されています。1つのみの対応です。')
      else:
        for atc in atc_list:
          await ctx.send(atc.url)
          
  @commands.command()
  async def send(ctg_id:int,
         
         
      
      
