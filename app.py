# import discord package 
# pip install discord
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from pysafebrowsing import SafeBrowsing
import re

load_dotenv()
intents = discord.Intents.default()
intents.members = True
bot=commands.Bot(command_prefix="$")

# event listeners 
@bot.event  
# defining function for on_ready function
# on_ready is predefined function under discord package 
async def on_ready():

    # prints in command line 
    print("Hi! I am online!")
    channel_id = int(os.getenv('WELCOME_CHANNEL_ID'))
    # fetching the general channel 
    general = bot.get_channel(channel_id)
    await general.send("Hello, Discord!, I am your assistant!")

# similarly we also have on_message event
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

@bot.event
async def on_member_join(member):
    guild_id = int(os.getenv('GUILD_ID'))
    channel_id = int(os.getenv('WELCOME_CHANNEL_ID'))
    guild = bot.get_guild(guild_id)
    channel = guild.get_channel(channel_id)
    await channel.send(f"Welcome to the server {member.mention} ! :partying_face:")
    await member.send(f"Welcome to the {guild.name} server, {member.name}! :partying_face:")

@bot.command(
    name="checklink", 
    brief="Use to check if a link is malicious or not", 
    help="Uses google safe browsing API to check if a link is safe or not.\nHow to use:\n$checklink www.TheLink.com")
async def checklinkfunc(ctx, link):
    s = SafeBrowsing('GOOGLE_SAFE_BROWSING_API_KEY')
    regex=r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url=re.findall(regex,link)
    try:
        link=url[0][0]
        r = s.lookup_urls([link])
        if r[link]["malicious"]==False:
            await ctx.channel.send(link+" **is not malicious**")
        elif r[link]["malicious"]==True:
            await ctx.channel.send(link+" **is malicious**")
        else:
            await ctx.channel.send("Something's is wrong")
    except:
        await ctx.channel.send("There was no link in your command\nExample command: ``check <pastethelinkhere>``")

bot.run(os.getenv('TOKEN'))
