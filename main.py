import os
import random
from typing import Final
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from keep_alive import keep_alive
from dotenv import load_dotenv

keep_alive()


intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='l!', intents=intents)
bot.help_command = None

@bot.event
async def on_ready():
   print('Logged in as {}'.format(bot.user.name))
   game = nextcord.Game("l!help")
   await bot.change_presence(
     status=nextcord.Status.do_not_disturb, 
     activity=game
   )
  
##################### [[ Commands ]] #####################
########################################################################################
@bot.slash_command(name="say", description="Gets the bot to say anything...", guild_ids=None)
async def aboutdea(interaction: Interaction, message: str):
    await interaction.response.defer()
    # Send the echoed message as the bot
    await interaction.followup.send(f"{message}")
########################################################################################
@bot.command(name="s-say")
async def ddddddddddddddddddddddddd(ctx, *, message: str):
    await ctx.message.delete()
    await ctx.send(f"{message}")
########################################################################################
@bot.slash_command(name="test", description="testing purposes only", guild_ids=None)
async def test(interaction: Interaction):
   await interaction.response.defer()
   await interaction.followup.send("TEST")
########################################################################################
@bot.slash_command(name="about", description="About the bot", guild_ids=None)
async def abbbs(interaction: Interaction):
    embed = nextcord.Embed(
        title='About Me',
        description='This bot is about a character that is in the yakuza series which is The Dragon of Dojima or Kazuma Kiryu (桐生 一馬, Kiryū Kazuma), also known as Joryu (浄龍, Jōryū) or Taichi Suzuki (鈴木 太一, Suzuki Taichi), which is the former primary protagonist of the Like a Dragon (formerly Yakuza) series. He is featured as a protagonist and playable character in the Yakuza series.',
        color=nextcord.Color.from_rgb(47, 49, 54),
    )
    embed.add_field(name='Status', value='The status of the bot, Working means that it is working fine and has no errors, Broken means the bot needs some fixes in order for it to work, Inactive means the bot is not working. This also contains the version of the bot and the changelogs.', inline=False)
    embed.add_field(name='The Current Status:', value='Working (No Errors)', inline=False)
    embed.add_field(name='Version', value='Version is 1.53', inline=False)
    embed.add_field(name='Changelogs', value='Added a new slash command: /insanity and a new command that also has the same features: l!insanity', inline=False)
    await interaction.response.defer()
    await interaction.followup.send(embed=embed)
########################################################################################
@bot.command(name="about")
async def about(ctx):
    embed = nextcord.Embed(
        title='About Me',
        description='This bot is about a character that is in the yakuza series which is The Dragon of Dojima or Kazuma Kiryu (桐生 一馬, Kiryū Kazuma), also known as Joryu (浄龍, Jōryū) or Taichi Suzuki (鈴木 太一, Suzuki Taichi), which is the former primary protagonist of the Like a Dragon (formerly Yakuza) series. He is featured as a protagonist and playable character in the Yakuza series.',
        color=nextcord.Color.from_rgb(47, 49, 54),
    )
    embed.add_field(name='Status', value='The status of the bot, Working means that it is working fine and has no errors, Broken means the bot needs some fixes in order for it to work, Inactive means the bot is not working. This also contains the version of the bot and the changelogs.', inline=False)
    embed.add_field(name='The Current Status:', value='Working (No Errors)', inline=False)
    embed.add_field(name='Version', value='Version is 1.53', inline=False)
    embed.add_field(name='Changelogs', value='Added a new slash command: /insanity and a new command that also has the same features: l!insanity', inline=False)
    await ctx.send(embed=embed)
########################################################################################
@bot.slash_command(name="yakuzafans", description="Yakuza fans be like", guild_ids=None)
async def yffs(interaction: nextcord.Interaction):
    try:
        file_path = 'Yakuza_fans_be_like.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='Yakuza_fans_be_like.mp4')
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command(name="yakuzafans")
async def yakuzafans(ctx):
  await ctx.send(file=nextcord.File('Yakuza_fans_be_like.mp4'))
########################################################################################
@bot.slash_command(name="insanity", description="Kiryu's Insanity", guild_ids=None)
async def insane(interaction: Interaction):
    try:
        file_path = '70431F28-2785-498B-8CF8-2FEFA415F355_2_2.mov'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='70431F28-2785-498B-8CF8-2FEFA415F355_2_2.mov')
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command(name="insanity")
async def insanity(ctx):
  await ctx.send(file=nextcord.File('70431F28-2785-498B-8CF8-2FEFA415F355_2.mov'))
########################################################################################
@bot.command()
async def help(ctx):
  try:
    embed = nextcord.Embed(
        title='__Commands__',
        description='These are the commands for the bot.',
        color=nextcord.Color.from_rgb(47, 49, 54),
    )

    embed.set_author(name="By Kiryu Kazuma and Darkin")

    embed.add_field(name='__Fun Commands__', value='Commands that are for fun', inline=False)     
    embed.add_field(name='l!dad', value='Roasts you for being a dumbass and thinking you have a dad.', inline=False)

    embed.add_field(name='l!bakamitai', value='Show\'s a video about kiryu singing baka mitai', inline=False)     
    embed.add_field(name='l!awakening', value='Show\'s a video about Kiryu\'s Legend Style "Dragon of Dojima" first appearance.', inline=False)     
    embed.add_field(name='l!sugarcoat', value='Show\'s a video about kiryu singing baka mitai', inline=False)     
    embed.add_field(name='l!egg', value='An egg command, pretty self explanatory', inline=False)     
    embed.add_field(name='l!kys', value='A command that shows low tier god roasting you', inline=False)     
    embed.add_field(name='l!tys', value='A command that shows low tier god complimenting you', inline=False)     
    embed.add_field(name='l!notsugarcoating', value='Show\'s a video of Kiryu not sugarcoating against majima', inline=False)     
    embed.add_field(name='l!scream', value='Show\'s a video singing today is a diamond but kiryu screaming credits to takayuki yagami for this idea', inline=False)     
    embed.add_field(name='l!roll', value='Rolls from a number to another number, pretty self explanatory', inline=False)                         
    embed.add_field(name='l!ip', value='Show\'s a video of captain underpants dancing while grabbing your ip', inline=False)     
    embed.add_field(name='l!china', value='Show\'s a video about the meme "China Airlines"', inline=False)   
    embed.add_field(name='l!dance', value='Show\'s 2 videos about kiryu dancing', inline=False)   
    embed.add_field(name='l!disagree', value='Show\'s a gif of ichiban not agreeing to your opinion', inline=False)   
    embed.add_field(name='l!yakuzillionaire', value='Show\'s a video of a meme of "yakuzillionaire"', inline=False)     
    embed.add_field(name='l!yakuza_fans', value='Show\'s a video of yakuza fans', inline=False)     
    embed.add_field(name='l!fact', value='Show\'s a random fact about the world.', inline=False)     
    embed.add_field(name='l!intro', value='Show\'s a video about kiryu\'s first appearance in Yakuza 7.', inline=False)     
    embed.add_field(name='l!joke', value='Tells you a random joke.', inline=False)     
    embed.add_field(name='l!solve', value='Solve\'s any math problem, it only supports multiplication, addition and division. For multiplication you\'ll you have to use an asterisk "*" ', inline=False)     
    embed.add_field(name='l!train', value='Show\'s a video about an edit of the A-Train', inline=False)     
    embed.add_field(name='l!n_word', value='Show\'s a video about the meme spot becoming black and saying ni-', inline=False)     
    embed.add_field(name='l!honestreaction', value='Show\'s a video about "My Honest Reaction 🗿"', inline=False)

    embed2 = nextcord.Embed(
        title='__Admin Commands__',
        description='Moderation commands for this bot.',
        color=nextcord.Color.from_rgb(47, 49, 54),
    )
    embed2.add_field(name='l!ban', value='Bans a member, self explanatory', inline=False)     
    embed2.add_field(name='l!kick', value='Pretty self explanatory', inline=False)     
    embed2.add_field(name='l!warn', value='Warns a member, if a member gets 3 warns they will get kicked if they get 6 warns they will get banned.', inline=False)     
    embed2.add_field(name='l!clearwarns', value='Clear\'s the warns of a user', inline=False)     
    embed2.add_field(name='l!lock', value='Locks a channel', inline=False)     
    embed2.add_field(name='l!unlock', value='Unlocks a channel', inline=False)     
    embed2.add_field(name='l!addrole', value='Add\'s a role to a user', inline=False)     
    embed2.add_field(name='l!removerole', value='Remove\'s a role from a user', inline=False)     
    embed2.add_field(name='l!slowmode', value='Add\'s a slowmode to a channel', inline=False)     
    embed2.add_field(name='l!clear', value='Clear\'s a specified amount of messages', inline=False)

    await ctx.author.send(embed=embed)
    await ctx.author.send(embed=embed2)

    await ctx.send('Check your dms')
  except nextcord.Forbidden:
    await ctx.send('Bro your dms closed')
########################################################################################
@bot.slash_command(name="help", description="Shows all of the commands", guild_ids=None)
async def showsallofthecommands(interaction: Interaction):
  embed = nextcord.Embed(
    title='__Commands__',
    description='These are the commands for the bot.',
    color=nextcord.Color.from_rgb(47, 49, 54),
  )

  embed.set_author(name="By Kiryu Kazuma and Darkin")

  embed.add_field(name='__Fun Commands__', value='Commands that are for fun', inline=False)     
  embed.add_field(name='l!dad', value='Roasts you for being a dumbass and thinking you have a dad.', inline=False)

  embed.add_field(name='l!bakamitai', value='Show\'s a video about kiryu singing baka mitai', inline=False)     
  embed.add_field(name='l!awakening', value='Show\'s a video about Kiryu\'s Legend Style "Dragon of Dojima" first appearance.', inline=False)     
  embed.add_field(name='l!sugarcoat', value='Show\'s a video about kiryu singing baka mitai', inline=False)     
  embed.add_field(name='l!egg', value='An egg command, pretty self explanatory', inline=False)     
  embed.add_field(name='l!kys', value='A command that shows low tier god roasting you', inline=False)     
  embed.add_field(name='l!tys', value='A command that shows low tier god complimenting you', inline=False)     
  embed.add_field(name='l!notsugarcoating', value='Show\'s a video of Kiryu not sugarcoating against majima', inline=False)     
  embed.add_field(name='l!scream', value='Show\'s a video singing today is a diamond but kiryu screaming credits to takayuki yagami for this idea', inline=False)     
  embed.add_field(name='l!roll', value='Rolls from a number to another number, pretty self explanatory', inline=False)                         
  embed.add_field(name='l!ip', value='Show\'s a video of captain underpants dancing while grabbing your ip', inline=False)     
  embed.add_field(name='l!china', value='Show\'s a video about the meme "China Airlines"', inline=False)   
  embed.add_field(name='l!dance', value='Show\'s 2 videos about kiryu dancing', inline=False)   
  embed.add_field(name='l!disagree', value='Show\'s a gif of ichiban not agreeing to your opinion', inline=False)   
  embed.add_field(name='l!yakuzillionaire', value='Show\'s a video of a meme of "yakuzillionaire"', inline=False)     
  embed.add_field(name='l!yakuza_fans', value='Show\'s a video of yakuza fans', inline=False)     
  embed.add_field(name='l!fact', value='Show\'s a random fact about the world.', inline=False)     
  embed.add_field(name='l!intro', value='Show\'s a video about kiryu\'s first appearance in Yakuza 7.', inline=False)     
  embed.add_field(name='l!joke', value='Tells you a random joke.', inline=False)     
  embed.add_field(name='l!solve', value='Solve\'s any math problem, it only supports multiplication, addition and division. For multiplication you\'ll you have to use an asterisk "*" ', inline=False)     
  embed.add_field(name='l!train', value='Show\'s a video about an edit of the A-Train', inline=False)     
  embed.add_field(name='l!n_word', value='Show\'s a video about the meme spot becoming black and saying ni-', inline=False)     
  embed.add_field(name='l!honestreaction', value='Show\'s a video about "My Honest Reaction 🗿"', inline=False)

  embed2 = nextcord.Embed(
    title='__Admin Commands__',
    description='Moderation commands for this bot.',
    color=nextcord.Color.from_rgb(47, 49, 54),
  )
  embed2.add_field(name='l!ban', value='Bans a member, self explanatory', inline=False)     
  embed2.add_field(name='l!kick', value='Pretty self explanatory', inline=False)     
  embed2.add_field(name='l!warn', value='Warns a member, if a member gets 3 warns they will get kicked if they get 6 warns they will get banned.', inline=False)     
  embed2.add_field(name='l!clearwarns', value='Clear\'s the warns of a user', inline=False)     
  embed2.add_field(name='l!lock', value='Locks a channel', inline=False)     
  embed2.add_field(name='l!unlock', value='Unlocks a channel', inline=False)     
  embed2.add_field(name='l!addrole', value='Add\'s a role to a user', inline=False)     
  embed2.add_field(name='l!removerole', value='Remove\'s a role from a user', inline=False)     
  embed2.add_field(name='l!slowmode', value='Add\'s a slowmode to a channel', inline=False)     
  embed2.add_field(name='l!clear', value='Clear\'s a specified amount of messages', inline=False)

  await interaction.response.defer()
  await interaction.followup.send(embed=embed)
  await interaction.followup.send(embed=embed2)
########################################################################################
@bot.slash_command(name="lock", description="Locks the channel. Administrative Permissions Required")
@commands.has_permissions(administrator=True)
async def locker(interaction: Interaction, channel: nextcord.TextChannel):
    overwrite = channel.overwrites_for(interaction.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
    await interaction.response.defer()
    await interaction.followup.send(f'channel {channel.mention} has been locked by {interaction.author.mention}')
@locker.error
async def lock_error(interaction: Interaction, error):
    if isinstance(error, commands.MissingPermissions):
        await interaction.response.send_message('u dont have perms :nerd:')
########################################################################################
@bot.command()
@commands.has_permissions(administrator=True)
async def locking(ctx, channel: nextcord.TextChannel):
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'channel {channel.mention} has been locked by {ctx.author.mention}')
@locking.error
async def lock_erroree(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('u dont have perms :nerd:')
########################################################################################
@bot.slash_command(name="kick", description="Kicks the specified member.")
@commands.has_permissions(administrator=True)
async def k(interaction: Interaction, member: nextcord.Member, reason: str = None):
    await interaction.guild.kick(member, reason=reason)
    await interaction.response.defer()
    await interaction.followup.send(f"User {member} has been kicked.")
@k.error
async def kickd_error(interaction: Interaction, error):
    if isinstance(error, commands.MissingPermissions):
      await interaction.response.defer()
      await interaction.followup.send('u dont have perms :nerd:')
########################################################################################
@bot.command()
@commands.has_permissions(kick_members=True)
async def kgg(ctx, member: nextcord.Member, reason: str = None):
    await ctx.guild.kick(member, reason=reason)
    await ctx.send(f"User {member} has been kicked.")

@kgg.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You don\'t have perms to use the kick command.')
########################################################################################
@bot.slash_command(name="bakamitai", description="Kiryu singing Bakamitai", guild_ids=None)
async def bm(interaction: Interaction):
    try:
        file_path = 'Yakuza_OST_-_Baka_Mitai__Kiryu_full_version.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='Yakuza_OST_-_Baka_Mitai__Kiryu_full_version.mp4')
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def bakamitai(ctx):
  await ctx.send(file=nextcord.File('Yakuza_OST_-_Baka_Mitai__Kiryu_full_version.mp4'))

########################################################################################
@bot.slash_command(name="notsugarcoating", description="Not Sugarcoating:", guild_ids=None)
async def ddea(interaction: Interaction):
    try:
        file_path = 'videoplayback.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='videoplayback.mp4')
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################

@bot.command()
async def notsugarcoating(ctx):
  await ctx.send(file=nextcord.File('videoplayback.mp4'))


########################################################################################
@bot.slash_command(name="sugarcoat", description="png of kiryu not sugarcoating", guild_ids=None)
async def sg(interaction: Interaction):
   await interaction.response.defer()
   await interaction.followup.send("<:not_sugarcoating:1125681011544559618>")
########################################################################################
@bot.command()
async def sugarcoat(ctx):
  await ctx.send("<:not_sugarcoating:1125681011544559618>")

########################################################################################
@bot.slash_command(name="widekiryu", description="Kiryu is an alpha male", guild_ids=None)
async def widekiryu(interaction: Interaction):
    try:
        file_path = 'widekiryu.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='widekiryu.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def alphamae(ctx):
  await ctx.send(file=nextcord.File('widekiryu.mp4'))

########################################################################################
@bot.slash_command(name="awakening", description="Kiryu is an alpha male", guild_ids=None)
async def beaaaaaaaaaaaaaaaaaa(interaction: Interaction):
    try:
        file_path = 'Dragon_of_Dojima_unlocked_-_Yakuza_0.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='Dragon_of_Dojima_unlocked_-_Yakuza_0.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def awakening(ctx):
  await ctx.send(file=nextcord.File('Dragon_of_Dojima_unlocked_-_Yakuza_0.mp4'))

########################################################################################
@bot.slash_command(name="treatyourself", description="Low Tier God saying treat yourself", guild_ids=None)
async def treatyourself(interaction: Interaction):
    try:
        file_path = 'treat_yourself.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='treat_yourself.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################

@bot.command()
async def tys(ctx):
  await ctx.send(file=nextcord.File('treat_yourself.mp4'))

########################################################################################
@bot.slash_command(name="kys", description="Low Tier God saying kill yourself", guild_ids=None)
async def zishe(interaction: Interaction):
    try:
        file_path = 'kys_with_vine_boom.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='kys_with_vine_boom.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def kys(ctx):
  await ctx.send(file=nextcord.File('kys_with_vine_boom.mp4'))

########################################################################################
@bot.slash_command(name="birbjima", description="Majima being a red bird lol", guild_ids=None)
async def vissssh(interaction: Interaction):
    try:
        file_path = 'Red_bird_meme_but_its_Majima.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='Red_bird_meme_but_its_Majima.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def birbjima(ctx):
  await ctx.send(file=nextcord.File('Red_bird_meme_but_its_Majima.mp4'))

########################################################################################
@bot.slash_command(name="chinese", description="Battle of chinese men", guild_ids=None)
async def whosingme(interaction: Interaction):
    try:
        file_path = 'nice_QTE.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='nice_QTE.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def chinese(ctx):
  await ctx.send(file=nextcord.File('nice_QTE.mp4'))
########################################################################################
@bot.slash_command(name="breaker", description="breaker style irl", guild_ids=None)
async def break_sssetgasstyle(interaction: Interaction):
    try:
        file_path = 'Breaker_Style.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='Breaker_Style.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def breaker(ctx):
  await ctx.send(file=nextcord.File('Breaker_Style.mp4'))
########################################################################################
@bot.slash_command(name="egg", description="egg", guild_ids=None)
async def niceeggbro(interaction: Interaction):
   await interaction.response.defer()
   await interaction.followup.send("egg 🗿🥚")
########################################################################################
@bot.command()
async def egg(ctx):
  await ctx.send("🥚")
########################################################################################
@bot.slash_command(name="disagree", description="I disagree", guild_ids=None)
async def broIhateyou(interaction: Interaction):
    try:
        file_path = 'Roblox_2023-07-10_21-26-23.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='Roblox_2023-07-10_21-26-23.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def disagree(ctx):

  await ctx.send(file=nextcord.File('Roblox_2023-07-10_21-26-23.mp4'))
########################################################################################
@bot.slash_command(name="nuke", description="STOP NUKING ☢😠", guild_ids=None)
async def nukeeing(interaction: Interaction):
   msg = random.choice([
      "Did you just try nuking the server nigga?",
      "Nigga, stop trying to nuke this server.",
      "You don't have a dad, nigga.",
      "Nigga, didn't I say stop trying?",
      "Im gonna kill yo ass nigga.",
   ])
   await interaction.response.defer()
   await interaction.followup.send(msg)
########################################################################################

@bot.command()
async def nuke(ctx):
  msg = random.choice([
    "Did you try nuking the server nigga",
    "Nigga, stop trying to nuke this server",
    "You don't have a dad, nigga",
    "Nigga, didn't I say stop trying?",
    "Im gonna kill yo ass nigga",
  ])
  await ctx.send(msg)

########################################################################################
@bot.slash_command(name="dad", description="Kiryu roasting you for not having a dad 😭", guild_ids=None)
async def easports(interaction: Interaction):
   await interaction.response.defer()
   await interaction.followup.send("You ugly ass, you don't have a dad, your dad left you for a reason lmao. Not just for milk but to not see you ever again hahaaaaa.")
########################################################################################
@bot.command()
async def dad(ctx):
  await ctx.send("You ugly ass, you don't have a dad, your dad left you, and you know that, you dumbass")
########################################################################################
@bot.slash_command(name="kiryuprowler", description="Meme of kiryu prowler", guild_ids=None)
async def kriyurolwer(interaction: Interaction):
    try:
        file_path = 'Kiryu_Prowler_meme.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='Kiryu_Prowler_meme.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def kiryuprowler(ctx):
  await ctx.send(file=nextcord.File("Kiryu_Prowler_meme.mp4"))
########################################################################################
@bot.slash_command(name="gun", description="Show's a meme of the insides of a gun", guild_ids=None)
async def broIhateyou(interaction: Interaction):
    try:
        file_path = 'gun.mov'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='gun.mov')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def gun(ctx):
  await ctx.send(file=nextcord.File('gun.mov'))
########################################################################################
@bot.slash_command(name="scream", description="Kiryu singing today is a diamond but he screams the lyrics lol", guild_ids=None)
async def broIhateyou(interaction: Interaction):
    try:
        file_path = 'Today_is_a_Diamond_but_Kiryu_Screams_The_Lyrics..mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='Today_is_a_Diamond_but_Kiryu_Screams_The_Lyrics..mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def scream(ctx):
  await ctx.send(file=nextcord.File('Today_is_a_Diamond_but_Kiryu_Screams_The_Lyrics..mp4'))
########################################################################################
@bot.slash_command(name="unlock", description="Unlocks a channel that you are in if it is locked", guild_ids=None)
@commands.has_permissions(administrator=True)
async def unlockeeeeeee(interaction: Interaction, channel: nextcord.TextChannel):
    overwrite = channel.overwrites_for(interaction.guild.default_role)
    overwrite.send_messages = None
    await channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
    await interaction.response.defer()
    await interaction.followup.send(f'Channel: {channel.mention} has been unlocked.')
@unlockeeeeeee.error
async def deea(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry but you do not have any permissions to unlock this channel 🤓')
########################################################################################
@bot.command()
@commands.has_permissions(administrator=True)
async def unlock(ctx):
    channel = ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = None
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'channel {channel.mention} has been unlocked')


@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('u dont have perms :nerd:')


########################################################################################
@bot.slash_command(name="ban", description="Bans a member.", guild_ids=None)
@commands.has_permissions(administrator=True)
async def banneed(interaction: Interaction, member: nextcord.Member, reason: str = None):
    await interaction.guild.ban(member, reason=reason)
    await interaction.response.defer()
    await interaction.followup.send(f"User {member} has been banned of this server.")
@banneed.error
async def bbanneedan_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You don\'t have perms to use the ban command.')
########################################################################################
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: nextcord.Member, reason: str = None):
    await ctx.guild.ban(member, reason=reason)
    await ctx.send(f"User {member} has been banned.")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You don\'t have perms to use the ban command.')


warns = {}

########################################################################################
@bot.slash_command(name="warn", description="Gets any member punished if they break the rules and warns them to not do it again.", guild_ids=None)
@commands.has_permissions(administrator=True)
async def warnde(interaction: Interaction, member: nextcord.Member, reason: str = None):
    if member not in warns:
        warns[member] = 0

    warns[member] += 1
    
    if warns[member] == 3:
      await interaction.guild.kick(member, reason=reason)
      await interaction.response.defer()
      await interaction.followup.send(f"User {member} has been kicked for exceeding the warn limit.")
    elif warns[member] == 6:
      await interaction.guild.ban(member, reason=reason)
      await interaction.response.defer()
      await interaction.followup.send(f"User {member} has been banned for exceeding the warn limit.")
    else:
      await interaction.response.defer()
      await interaction.followup.send(f"User {member} has been warned for {reason}.")

@warnde.error
async def warn_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You don\'t have perms to use the warn command.')
########################################################################################

@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: nextcord.Member, reason: str = None):
    if member not in warns:
        warns[member] = 0

    warns[member] += 1

    if warns[member] == 3:
        await ctx.guild.kick(member, reason=reason)
        await ctx.send(f"User {member} has been kicked for exceeding the warn limit.")
    elif warns[member] == 6:
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"User {member} has been banned for exceeding the warn limit.")
    else:
        await ctx.send(f"User {member} has been warned for {reason}.")

@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You don\'t have perms to use the warn command.')
########################################################################################
@bot.slash_command(name="roll", description="Lets the bot pick any number from what you've picked", guild_ids=None)
async def edda(interaction: Interaction, min: int, max: int):
   if min > max:
      await interaction.response.defer()
      await interaction.followup.send("The minimum number must be less than or equal to the maximum number.")
      return
   number = random.randint(min, max)
   await interaction.response.defer()
   await interaction.followup.send(f"{number}")
########################################################################################
@bot.command()
async def roll(ctx, min: int, max: int):
    if min > max:
        await ctx.send("The minimum number must be less than or equal to the maximum number.")
        return

    number = random.randint(min, max)
    await ctx.send(f"{number}")

########################################################################################
@bot.slash_command(name="clearwarns", description="Clears all of the warns of a specified user.", guild_ids=None)
@commands.has_permissions(administrator=True)
async def broIhateyou(interaction: Interaction, member: nextcord.Member):
   if member not in warns:
      await interaction.response.defer()
      await interaction.followup.send()
      return
   
   warns[member] = 0

   await interaction.response.defer()
   await interaction.followup.send(f"User: {member}'s warns have now been cleared.")
########################################################################################
@bot.command()
@commands.has_permissions(administrator=True)
async def clearwarns(ctx, member: nextcord.Member):
    if member not in warns:
        await ctx.send(f"User {member} has no warns.")
        return

    warns[member] = 0
    await ctx.send(f"User {member}'s warns have been cleared.")

########################################################################################
@bot.slash_command(name="joke", description="Jokes around.", guild_ids=None)
async def jokde(interaction: Interaction):
  joke = random.choice([
    "What do you call a fish with no eyes? Fsh!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why did the bicycle fall over? Because it was two tired!",
    "What do you call a fish with no eyes? Fsh!",
  ])
  await interaction.response.defer()
  await interaction.followup.send(joke)
########################################################################################

@bot.command()
async def joke(ctx):
  joke = random.choice([
    "What do you call a fish with no eyes? Fsh!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why did the bicycle fall over? Because it was two tired!",
    "What do you call a fish with no eyes? Fsh!",
  ])
  await ctx.send(joke)

########################################################################################
@bot.slash_command(name="fact", description="Fun facts you can learn from the bot", guild_ids=None)
async def factss(interaction: Interaction):
  fact = random.choice([
    "The population of the earth is about 8 billion people.",
    "The sun is about 93 million miles from Earth.",
    "The tallest mountain in the world is Mount Everest, which is 29,031 feet tall.",
    "The deepest ocean in the world is the Mariana Trench, which is about 36,000 feet deep.",
    "The fastest animal on Earth is the peregrine falcon, which can fly at speeds of up to 242 mph.",
    "The Universe is 13.7 billion years old now.",
  ])
  await interaction.response.defer()
  await interaction.followup.send(f"{fact}")
########################################################################################
@bot.command()
async def fact(ctx):
  fact = random.choice([
    "The population of the earth is about 8 billion people.",
    "The sun is about 93 million miles from Earth.",
    "The tallest mountain in the world is Mount Everest, which is 29,031 feet tall.",
    "The deepest ocean in the world is the Mariana Trench, which is about 36,000 feet deep.",
    "The fastest animal on Earth is the peregrine falcon, which can fly at speeds of up to 242 mph.",
    "The Universe is 13.7 billion years old now.",
  ])
  await ctx.send(fact)

########################################################################################
@bot.slash_command(name="addrole", description="Adds a role to a member. Opposite version: /removerole", guild_ids=None)
@commands.has_permissions(manage_roles=True)
async def addroled(interaction: Interaction, member: nextcord.Member, role: nextcord.Role):
   await member.add_roles(role)
   await interaction.response.defer()
   await interaction.followup.send(f"Added the {role.name} role to {member.name}")
########################################################################################
@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: nextcord.Member, role: nextcord.Role):
  await member.add_roles(role)
  await ctx.send(f"Added the {role.name} role to {member.name}")

########################################################################################
@bot.slash_command(name="removerole", description="Removes a role from a member. Opposite version: /addrole", guild_ids=None)
@commands.has_permissions(manage_roles=True)
async def addroleddd(interaction: Interaction, member: nextcord.Member, role: nextcord.Role):
   await member.add_roles(role)
   await interaction.response.defer()
   await interaction.followup.send(f"Added the {role.name} role to {member.name}")
########################################################################################
@bot.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: nextcord.Member, role: nextcord.Role):
  await member.remove_roles(role)
  await ctx.send(f"Removed the {role.name} role from {member.name}")

########################################################################################
@bot.slash_command(name="china", description="China airlines be liek:", guild_ids=None)
async def broIhateyou(interaction: Interaction):
    try:
        file_path = 'Snaptik.app_7226749375664393498.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='Snaptik.app_7226749375664393498.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################

@bot.command()
async def china(ctx):
    await ctx.send(file=nextcord.file('Snaptik.app_7226749375664393498.mp4'))

########################################################################################
@bot.slash_command(name="ip", description="This isn't real tho lol", guild_ids=None)
async def dxxxxxxxxxxxx(interaction: Interaction):
    try:
        file_path = 'Captain_Underpants_dancing_while_grabbing_your_ip.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='Captain_Underpants_dancing_while_grabbing_your_ip.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def ip(ctx):
    await ctx.send(file=nextcord.File('Captain_Underpants_dancing_while_grabbing_your_ip.mp4'))

########################################################################################
@bot.slash_command(name="kiryu", description="Kiryu's Yakuza Like A Dragon Intro.", guild_ids=None)
async def dxdxdase(interaction: Interaction):
    try:
        file_path = 'Yakuza__Like_A_Dragon_-_Kiryu_Intro.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='Yakuza__Like_A_Dragon_-_Kiryu_Intro.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def kiryu(ctx):
    await ctx.send(file=nextcord.File('Yakuza__Like_A_Dragon_-_Kiryu_Intro.mp4'))

########################################################################################
@bot.slash_command(name="intro", description="Kiryu's first entrance", guild_ids=None)
async def deaaaaaaaaa(interaction: Interaction):
    try:
        file_path = '0708_11.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='0708_11.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def intro(ctx):
    await ctx.send(file=nextcord.File('0708_11.mp4'))

########################################################################################
@bot.slash_command(name="dance", description="Video of kiryu dancing", guild_ids=None)
async def broIhateyou(interaction: Interaction):
    try:
        file_path = 'k.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='k.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def dance(ctx):
  await ctx.send('k.mp4')

########################################################################################
@bot.slash_command(name="slowmode", description="Sets a cooldown.", guild_ids=None)
@commands.has_permissions(administrator=True)
async def broIhateyodeaud(interaction: Interaction, channel: nextcord.TextChannel, cooldown: int):
    await channel.edit(slowmode_delay=cooldown)
    await interaction.response.defer()
    await interaction.followup.send(f'Slowmode set to {cooldown} messages per second in {channel.name}')
########################################################################################
@bot.command(name='slowmode', help='Slowmodes a specific channel with a specific amount of message per second')
@commands.has_permissions(administrator=True)
async def slowmode(ctx, channel: nextcord.TextChannel, message_per_second: int):
    await channel.edit(slowmode_delay=message_per_second)
    await ctx.send(f'Slowmode set to {message_per_second} messages per second in {channel.name}')
########################################################################################
@bot.slash_command(name="yakuzillionaire", description="Yakuza 4 thing", guild_ids=None)
async def broIhateyou(interaction: Interaction):
    try:
        file_path = 'y4_rem.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='y4_rem.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def yakuzillionaire(ctx):
    await ctx.send(file=nextcord.File('y4_rem.mp4'))
########################################################################################
@bot.slash_command(name="train", description="Edit of A-Train", guild_ids=None)
async def broIhateyodddddu(interaction: Interaction):
    try:
        file_path = '0708_12.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='0708_12.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def train(ctx):

  await ctx.send(file=nextcord.File('0708_12.mp4'))

########################################################################################
@bot.slash_command(name="clear", description="Purges the amount specified :", guild_ids=None)
async def broIhddateyou(interaction: Interaction, number: int):
    channel = interaction.channel
    await channel.purge(limit=number)
    await interaction.response.defer()
    await interaction.followup.send(f"Purged {number} messages.")
########################################################################################
@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, number: int):
  """Clears a specific amount of messages."""
  channel = ctx.channel
  await channel.purge(limit=number)
  await ctx.send(f"Deleted {number} messages.")

########################################################################################
@bot.slash_command(name="n_word", description="Spot saying the n word 🤯", guild_ids=None)
async def nwordd(interaction: Interaction):
    try:
        file_path = 'IM_SAYING_THE_N_WORD.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='IM_SAYING_THE_N_WORD.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def n_word(ctx):

  await ctx.send(file=nextcord.File('IM_SAYING_THE_N_WORD.mp4'))

########################################################################################
@bot.slash_command(name="honestreaction", description="My honest reaction:", guild_ids=None)
async def my_honest_reaction_4K(interaction: Interaction):
    try:
        file_path = 'my_honest_reaction_4K.mp4'
        
        if not os.path.isfile(file_path):
            await interaction.response.send_message("File not found.")
            return

        with open(file_path, 'rb') as file:
            file_to_send = nextcord.File(file, filename='my_honest_reaction_4K.mp4')
            # Defer the response before sending the file
            await interaction.response.defer()
            await interaction.followup.send(file=file_to_send)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")
########################################################################################
@bot.command()
async def honestreaction(ctx):

    await ctx.send(file=nextcord.File('my_honest_reaction_4K.mp4'))

########################################################################################
@bot.slash_command(name="solve", description="Solves basic problems", guild_ids=None)
async def solveeea(interaction: Interaction, equation):
  try:
    solution = str(eval(equation))
  except Exception as e:
    solution = "Invalid equation."
    print(e)
  await interaction.response.defer()
  await interaction.followup.send(f"The solution to the equation is {solution}.")
########################################################################################
@bot.command()
async def solve(ctx, equation):
  """Solve a math equation."""
  try:
    solution = str(eval(equation))
  except Exception as e:
    solution = "Invalid equation."
    print(e)
  await ctx.send(f"The solution to the equation is {solution}.")
# RUN THE BOT
bot.run(os.environ['TOKEN'])
