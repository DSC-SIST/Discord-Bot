# import discord package 
# pip install discord
import discord
from discord.ext import commands
from dotenv import load_dotenv
import json
import os
from urllib import request



load_dotenv()

intents = discord.Intents.default()
intents.members = True
# this is our bot
# bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=['$','--','>',"!"])
bot.remove_command("help")

JOKE_API = os.getenv("JOKE_API")
TOKEN = os.getenv("TOKEN")
GENERAL = os.getenv("GENERAL_CHANNEL_ID")
WELCOME = os.getenv('WELCOME_CHANNEL_ID')
GUILD = os.getenv("GUILD_ID")




# api request for joke 
def getJoke():
    url = request.urlopen(JOKE_API)
    data = url.read()
    jsonData = json.loads(data)
    # print(jsonData)
    for joke in jsonData:
        setup = joke["setup"]
        punchline = joke["punchline"]
        laughingFace = "\U0001F606"
    joke = f"setup: {setup}" "\n" f"Punchline : {punchline}\t{laughingFace} "
    # print(f"Setup : {setup}")
    # print(f"Punchline : {punchline}")
    return joke
# getJoke()
 

@bot.command(name="help")
async def help(context):
    myEmbed = discord.Embed(title="Commands",color=0x00ff00)
    # myEmbed.add_field(name="Prefix",value="!, $, >, --",inline=False)
    myEmbed.add_field(name="hello",value="Says Hello back",inline=False)
    myEmbed.add_field(name="Hello Alex",value="Greets back",inline=False)
    myEmbed.add_field(name="joke",value="Returns a programming joke",inline=False)
    myEmbed.set_author(name="Prefix : !, $, >, --")
    await context.message.channel.send(embed=myEmbed)

@bot.command(name="joke")
async def joke(context):
    joke = getJoke()
    await context.message.channel.send(joke)

@bot.command(name="Hello_Alex")
async def HelloAlex(message):
    user = message.author.mention
    # print(type(user))
    await message.channel.send(f"Hello, {user}, Hope you are doing good.")

# event listeners 
@bot.event  
# defining function for on_ready function
# on_ready is predefined function under discord package 
async def on_ready():

    print("Hi! I am online!")
    # fetching the Welcome channel
    channel_id = int(WELCOME)
    welcome = bot.get_channel(channel_id)
    await welcome.send("Hello, Discord!, I am your assistant!")

# similarly we also have on_message event
@bot.event
async def on_message(message):
    # if someone types "Hello Bot" in general channel Bot will send Hello {username}
    if message.content == "Hello Alex":
        # general = bot.get_channel(int(os.getenv('GENERAL_CHANNEL_ID')))
        user = message.author.mention
        # print(type(user))
        await message.channel.send(f"Hello, {user}, Hope you are doing good.")

    # if someone requests a joke by typing "!joke" bot will send a joke 
    # if message.content == "!joke":
    #     joke = getJoke()
    #     await message.channel.send(joke)

    if message.author == bot.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    guild_id = int(GUILD)
    channel_id = int(WELCOME)
    guild = bot.get_guild(guild_id)
    channel = bot.get_channel(channel_id)
    await channel.send(f"Welcome to the server {member.mention} ! :partying_face:")
    await member.send(f"Welcome to the {guild.name} server, {member.name}! :partying_face:")


# run the bot server by passing the token in the string 
bot.run(TOKEN)