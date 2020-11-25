import discord
from discord.ext import commands
import 

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
  async def send(self,ctx,ctg_id:int):
    #カテゴリの取得
    ctg = ctx.guild.get_channel(ctg_id)
    if ctg == None:
      await ctx.send('カテゴリの取得に失敗しました')
      return
    elif ctg.type != discord.ChannelType.category:
      await ctx.send('カテゴリIDを指定してください')
      return
    elif ctg.type == discord.ChannelType.category:
      embed = discord.Embed(title='送信オプションの確認',description='メンション確認',colour=discord.Colour.blue())
      embed.add_field(name='everyoneメンションする',value='\u2705',inline=False)
      embed.add_field(name='everyoneメンションしない',value='\u274E',inline=False)
      mention_msg = await ctx.send(embed=embed)
      await mention_msg.add_reaction('\u2705')
      await mention_msg.add_reaction('\u274E')
      await mention_msg.add_reaction('\u26D4')
      
      def check(reaction,user):
        return user==ctx.author and reaction.message==mention_msg
      
      try:
        reaction,user = await self.bot.wait_for('reaction_add',timeout=60,check=check)
      except asyncio.TimeoutError:
        await ctx.send('60秒間無操作だったため操作を中止しました。')
      else:
        if str(reaction.emoji) == '\u2705':
          do_mention = True
        elif str(reaction.emoji) == '\u274E':
          do_mention = False
        elif str(reaction.emoji) == '\u26D4':
          await ctx.send('終了しました')
          return
      type_msg = await ctx.send('送信メッセージをこのチャンネルに送信してください。')
      
      def msgcheck(m):
        return m.author == ctx.author and m.channnel == ctx.channel
      
      try:
        m = await self.bot.wait_for('message',timeout=60,check=msgcheck)
      except asyncio.TimeoutError:
        
         
      
      
