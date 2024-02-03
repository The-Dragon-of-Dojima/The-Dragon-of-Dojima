import os
import random

import discord
from discord.ext import commands
from keep_alive import keep_alive


keep_alive()


intents = discord.Intents.default()
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='l!', intents=intents)

bot.help_command = None

@bot.event
async def on_ready():
   print('Logged in as {}'.format(bot.user.name))
   game = discord.Game("l!help")
   await bot.change_presence(
     status=discord.Status.do_not_disturb, 
     activity=game
   )
   try:
     synced = await bot.tree.sync()
     print(f'Synced {len(synced)} Commands')
   except Exception as e:
     print(e)
     print("Error 404")


##################### [[ Slash Commands ]] #####################


@bot.tree.command(name="about", description="Information on the bot. This also has an alternative version: l!about")
async def about1(interaction: discord.Interaction):
  embed = discord.Embed(
      title='About Me',
      description='This bot is about a character that is in the yakuza series which is The Dragon of Dojima or Kazuma Kiryu (桐生 一馬, Kiryū Kazuma), also known as Joryu (浄龍, Jōryū) or Taichi Suzuki (鈴木 太一, Suzuki Taichi), which is the former primary protagonist of the Like a Dragon (formerly Yakuza) series. He is featured as a protagonist and playable character in the Yakuza series.',
      color=discord.Color.from_rgb(47, 49, 54),
  )
  embed.add_field(name='Status', value='The status of the bot, Working means that it is working fine and has no errors, Broken means the bot needs some fixes in order for it to work, Inactive means the bot is not working. This also contains the version of the bot and the changelogs.', inline=False)
  embed.add_field(name='The Current Status:', value='Working (No Errors)', inline=False)
  embed.add_field(name='Version', value='Version is 1.53', inline=False)
  embed.add_field(name='Changelogs', value='Added a new slash command: /insanity and a new command that also has the same features: l!insanity', inline=False)
  await interaction.response.send_message(embed=embed)



@bot.command(name="about", description="Show's what is the bot all about, this contains the version, status, and a lot more!. This also has an alternative version: l!about")
async def about(ctx):
    embed = discord.Embed(
        title='About Me',
        description='This bot is about a character that is in the yakuza series which is The Dragon of Dojima or Kazuma Kiryu (桐生 一馬, Kiryū Kazuma), also known as Joryu (浄龍, Jōryū) or Taichi Suzuki (鈴木 太一, Suzuki Taichi), which is the former primary protagonist of the Like a Dragon (formerly Yakuza) series. He is featured as a protagonist and playable character in the Yakuza series.',
        color=discord.Color.from_rgb(47, 49, 54),
    )
    embed.add_field(name='Status', value='The status of the bot, Working means that it is working fine and has no errors, Broken means the bot needs some fixes in order for it to work, Inactive means the bot is not working. This also contains the version of the bot and the changelogs.', inline=False)
    embed.add_field(name='The Current Status:', value='Working (No Errors)', inline=False)
    embed.add_field(name='Version', value='Version is 1.53', inline=False)
    embed.add_field(name='Changelogs', value='Added a new slash command: /insanity and a new command that also has the same features: l!insanity', inline=False)
    await ctx.send(embed=embed)

@bot.tree.command(name="hello", description="Greets you politely.")
async def hello(interaction: discord.Interaction):
  eae = random.choice([
    "Hello",
    "Wassup",
    "Yo",
    "Hi Mate",
    "Sup",
    "Hi",
    "Good Morning",
    "Good Afternoon",
    "Good Evening",
    "Mornin', lads!",
    "Great to see you around, mate!",
    "Nice to see you, lad",
    "Good to see you!",
    "Howdy!",
    "Greetings, mate.",
    "こんにちは",
    "ワサップ",
    "よ",
    "やあ",
    "すする",
    "やあ",
    "おはよう",
    "こんにちは",
    "こんばんは",
  ])
  await interaction.response.send_message(eae)

@bot.tree.command(name="nuke", description="Roasts you for trying to nuke the server")
async def nuke(interaction: discord.Interaction):
  nukemsg = random.choice([
    "Did you try nuking the server, well you can't",
    "Stop trying to nuke the server.",
    "You don't have a dad, nigga",
    "Im deadass, stop trying to nuke the server.",
    "Stop with the nuking, god damn.",
    "Shut up, nigga",
  ])
  await interaction.response.send_message(nukemsg)


@bot.tree.command(name="ten_years", description="Show's nishiki saying the classical meme ten years in the joint.")
async def ten_years(interaction: discord.Interaction):
  await interaction.response.send_message(file=discord.File('videoplayback_3.mp4'))
@bot.tree.command(name="yakuzafans", description="PS: This has an alternative version: l!yakuzafans")
async def yakuzafans(interaction: discord.Interaction):
  await interaction.response.send_message(file=discord.File('Yakuza fans be like.mp4'))

@bot.command(name="yakuzafans", description="PS: This has an alternative version: l!yakuzafans")
async def yakuzafans1(ctx):
  await ctx.send(file=discord.File('Yakuza fans be like.mp4'))
@bot.command(name="chinese", description="The battle of the chinese man")
async def chinese(interaction: discord.Interaction):
  await interaction.response.send_message(file=discord.File('nice_QTE.mp4'))
@bot.tree.command(name="insanity", description="Show's a video of kiryu beating up koji shindo. PS: This has an alternative version: l!insanity")
async def insanity(interaction: discord.Interaction):
  await interaction.response.send_message(file=discord.File('70431F28-2785-498B-8CF8-2FEFA415F355_2.mov'))

@bot.command(name="insanity", description="Show's a video of kiryu being insane")
async def insanity(ctx):
  await ctx.send(file=discord.File('70431F28-2785-498B-8CF8-2FEFA415F355_2.mov'))

@bot.tree.command(name="tigerdrop", description="Tiger drop in a nutshell.")
async def tigerdrop(interaction: discord.Interaction):
  await interaction.response.send_message(file=discord.File('FIXED_Yakuza_Kiwami_Tiger_Drop_in_a_Nutshell.mp4'))

@bot.tree.command(name="disagree", description="The disagree command comes back but with a punch?!")
async def disagree(interaction: discord.Interaction):

  await interaction.response.send_message(file=discord.File('Roblox_2023-07-10_21-26-23.mp4'))

@bot.tree.command(name="chinese", description="The battle of the chinese man")
async def chinese(interaction: discord.Interaction):

  await interaction.response.send_message(file=discord.File('nice_QTE.mp4'))

@bot.tree.command(name="kiryuchan", description="A compilation of majima saying ''Kiryu Chan''")
async def kiryuchan(interaction: discord.Interaction):

  await interaction.response.send_message(file=discord.File('ekc.mp4'))

@bot.tree.command(name="kiryuprowler", description="Kiryu doesn't approve of you.")
async def kiryuprowler(interaction: discord.Interaction):

  await interaction.response.send_message(file=discord.File('Kiryu_Prowler_meme.mp4'))

@bot.tree.command(name="widekiryu", description="Show's a video of wide kiryu")
async def widekiryu(interaction: discord.Interaction):

  await interaction.response.send_message(file=discord.File('Kiryu is an Alpha male.mp4'))

@bot.tree.command(name="babyrocky", description="Show's the whole story of baby rocky's death. 😢")
async def babyrocky(interaction: discord.Interaction):

  await interaction.response.send_message("On 6/29 2023 reather got a new pet a baby chicken and one day his big brother died and he was calling him all day more days later hes younger brother died to so reather was gonna kill his dog now reather is depressed")

@bot.tree.command(name="n_word", description="The Spot saying the n word?!!1")
async def n_word(interaction: discord.Interaction):

  await interaction.response.send_message(file=discord.File('IM_SAYING_THE_N_WORD.mp4'))
##################### [[ Commands ]] #####################

@bot.command()
async def help(ctx):
  try:
    embed = discord.Embed(
        title='__Commands__',
        description='These are the commands for the bot.',
        color=discord.Color.from_rgb(47, 49, 54),
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

    embed2 = discord.Embed(
        title='__Admin Commands__',
        description='Moderation commands for this bot.',
        color=discord.Color.from_rgb(47, 49, 54),
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
  except discord.Forbidden:
    await ctx.send('Bro your dms closed')


@bot.command()
@commands.has_permissions(administrator=True)
async def lock(ctx):
    channel = ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'channel {channel.mention} has been locked by {ctx.author.mention}')

@lock.error
async def lock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('u dont have perms :nerd:')
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, reason: str = None):
    await ctx.guild.kick(member, reason=reason)
    await ctx.send(f"User {member} has been kicked.")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You don\'t have perms to use the kick command.')
@bot.command()
async def bakamitai(ctx):
  await ctx.send(file=discord.File('Yakuza_OST_-_Baka_Mitai__Kiryu_full_version.mp4'))


@bot.command()
async def notsugarcoating(ctx):
  await ctx.send(file=discord.File('videoplayback.mp4'))


@bot.command()
async def sugarcoat(ctx):
  await ctx.send("<:not_sugarcoating:1125681011544559618>")


@bot.command()
async def awakening(ctx):
  await ctx.send(file=discord.File('Dragon_of_Dojima_unlocked_-_Yakuza_0.mp4'))


@bot.command()
async def tys(ctx):
  await ctx.send(file=discord.File('treat_yourself.mp4'))


@bot.command()
async def kys(ctx):
  await ctx.send(file=discord.File('kys_with_vine_boom.mp4'))


@bot.command()
async def birbjima(ctx):
  await ctx.send(file=discord.File('Red_bird_meme_but_its_Majima.mp4'))


@bot.command()
async def breaker(ctx):
  await ctx.send(file=discord.File('Breaker_Style.mp4'))


@bot.command()
async def egg(ctx):
  await ctx.send("🥚")


@bot.command()
async def disagree(ctx):

  await ctx.send(file=discord.File('Roblox_2023-07-10_21-26-23.mp4'))


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


@bot.command()
async def dad(ctx):
  await ctx.send("You ugly ass, you don't have a dad, your dad left you, and you know that, you dumbass")
@bot.command()
async def kiryuprowler(ctx):
  await ctx.send(file=discord.File("Kiryu_Prowler_meme.mp4"))
@bot.command()
async def gun(ctx):
  await ctx.send(file=discord.File('gun.mov'))
@bot.command(name='say')
async def say(ctx, *, message):
  await ctx.send(message)
  # Delete the user's command message
  await ctx.message.delete()
  
@bot.command()
async def scream(ctx):
  await ctx.send(file=discord.File('Today_is_a_Diamond_but_Kiryu_Screams_The_Lyrics..mp4'))

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


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, reason: str = None):
    await ctx.guild.ban(member, reason=reason)
    await ctx.send(f"User {member} has been banned.")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You don\'t have perms to use the ban command.')


warns = {}

@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member, reason: str = None):
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
@bot.command()
async def roll(ctx, min: int, max: int):
    if min > max:
        await ctx.send("The minimum number must be less than or equal to the maximum number.")
        return

    number = random.randint(min, max)
    await ctx.send(f"{number}")

@bot.command()
@commands.has_permissions(administrator=True)
async def clearwarns(ctx, member: discord.Member):
    if member not in warns:
        await ctx.send(f"User {member} has no warns.")
        return

    warns[member] = 0
    await ctx.send(f"User {member}'s warns have been cleared.")


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


@bot.command()
@commands.has_permissions(administrator=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
  await member.add_roles(role)
  await ctx.send(f"Added the {role.name} role to {member.name}")

@bot.command()
@commands.has_permissions(administrator=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
  await member.remove_roles(role)
  await ctx.send(f"Removed the {role.name} role from {member.name}")


@bot.command()
async def china(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1107240352705949766/1126435595145715712/Snaptik.app_7226749375664393498.mp4")

@bot.command()
async def ip(ctx):
    await ctx.send(file=discord.File('Captain_Underpants_dancing_while_grabbing_your_ip.mp4'))

@bot.command()
async def kiryu(ctx):
    await ctx.send(file=discord.File('Yakuza__Like_A_Dragon_-_Kiryu_Intro.mp4'))

@bot.command()
async def intro(ctx):
    await ctx.send(file=discord.File('0708_11.mp4'))

@bot.command()
async def dance(ctx):
  msg2 = random.choice([
    "https://cdn.discordapp.com/attachments/1127852266494369852/1132134126045114398/All_Video_Downloader_youtube_1688701220681.mp4",
    "https://cdn.discordapp.com/attachments/1127852266494369852/1132134125302710292/All_Video_Downloader_youtube_1688701454035.mp4",
  ])
  await ctx.send(msg2)

@bot.command(name='slowmode', help='Slowmodes a specific channel with a specific amount of message per second')
@commands.has_permissions(administrator=True)
async def slowmode(ctx, channel: discord.TextChannel, message_per_second: int):
    await channel.edit(slowmode_delay=message_per_second)
    await ctx.send(f'Slowmode set to {message_per_second} messages per second in {channel.name}')


@bot.command()
async def yakuzillionaire(ctx):
    await ctx.send(file=discord.File('y4_rem'))

@bot.command()
async def yakuza_fans(ctx):
    await ctx.send(file=discord.File('Yakuza fans be like.mp4'))

@bot.command()
async def eeeae(ctx):

    await ctx.send("https://media.tenor.com/67LIumILNRsAAAAC/ltg-low-tier-god.gif")

@bot.command()
async def eeeea(ctx):

  await ctx.send(file=discord.File('videoplayback_1.mp4'))


@bot.command()
async def deathe(ctx):

  await ctx.send(file=discord.File('my_honest_reaction_4K.mp4'))


@bot.command()
async def train(ctx):

  await ctx.send(file=discord.File('O708_11.mp4'))

@bot.command()
@commands.is_owner()
async def death(ctx):

  await ctx.send(file=discord.File('Breaker_Style.mp4'))

@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, number: int):
  """Clears a specific amount of messages."""
  channel = ctx.channel
  await channel.purge(limit=number)
  await ctx.send(f"Deleted {number} messages.")


@bot.command()
async def n_word(ctx):

  await ctx.send(file=discord.File('IM_SAYING_THE_N_WORD.mp4'))


@bot.command()
async def niggaeea(ctx):

    await ctx.send(file=discord.File('IM_SAYING_THE_N_WORD.mp4'))

@bot.command()
async def honestreaction(ctx):

    await ctx.send(file=discord.File('my_honest_reaction_4K.mp4'))

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
token = os.environ.get('TOKEN')
bot.run(token)
