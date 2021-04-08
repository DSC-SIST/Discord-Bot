# import discord package 
# pip install discord
import discord
from dotenv import load_dotenv
import os
from pysafebrowsing import SafeBrowsing
import re

load_dotenv()
intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)

def linkcheck(msg):
    s = SafeBrowsing('GOOGLE_SAFE_BROWSING_API_KEY')
    regex=r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url=re.findall(regex,msg)
    try:
        link=url[0][0]
        r = s.lookup_urls([link])
        if r[link]["malicious"]==False:
            return link+" **is not malicious**"
        elif r[link]["malicious"]==True:
            return link+" **is malicious**"
        else:
            return "Something's is wrong"
    except:
        return "There was no link in your command\nExample command: ``check <pastethelinkhere>``"

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

    if message.content.startswith('check'):
        await message.channel.send(linkcheck(message.content))

@bot.event
async def on_member_join(member):
    guild_id = int(os.getenv('GUILD_ID'))
    channel_id = int(os.getenv('WELCOME_CHANNEL_ID'))
    guild = bot.get_guild(guild_id)
    channel = guild.get_channel(channel_id)
    await channel.send(f"Welcome to the server {member.mention} ! :partying_face:")
    await member.send(f"Welcome to the {guild.name} server, {member.name}! :partying_face:")

bot.run(os.getenv('TOKEN'))
