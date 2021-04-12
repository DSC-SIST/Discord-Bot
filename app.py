# import discord package 
# pip install discord
import datetime
import discord
from dotenv import load_dotenv
import os
from wordnik import *

load_dotenv()
intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)

def wordOfDay():
	now=datetime.datetime.now()
	today=str(now.year)+'-'+str(now.month)+'-'+str(now.day)
	url='http://api.wordnik.com:80/v4/words.json/wordOfTheDay?date='+today+'&api_key=d52b63b6880f17811310d0fbd3b0d3a8ef163a248f58dc831'
	response=urllib.urlopen(url)
	word=json.load(response)
	x=word['word']
	word_of_the_day=bytes(x)
	y=word['note']
	note=bytes(y)
	meaning=word['definitions'][0]['text']
	print "*****************************************"
	print "The word of the day is: "+word_of_the_day
	print "Meaning: "+meaning
	print "Note : "+note
	print "*****************************************"
    result = f"The word of the day is: {word_of_the_day}"
wordOfDay()

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

    if message.content == "$word":
        res=wordOfDay()
        await message.channel.send(res)

@bot.event
async def on_member_join(member):
    guild_id = int(os.getenv('GUILD_ID'))
    channel_id = int(os.getenv('WELCOME_CHANNEL_ID'))
    guild = bot.get_guild(guild_id)
    channel = guild.get_channel(channel_id)
    await channel.send(f"Welcome to the server {member.mention} ! :partying_face:")
    await member.send(f"Welcome to the {guild.name} server, {member.name}! :partying_face:")

bot.run(os.getenv('TOKEN'))
