# import discord package 
# pip install discord
import discord
from urllib import request
import json

# this is our bot 
bot = discord.Client()

# api request for joke 
def getJoke():
    url = request.urlopen("https://official-joke-api.appspot.com/jokes/programming/random")
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
 
# event listeners 
@bot.event  
# defining function for on_ready function
# on_ready is predefined function under discord package 
async def on_ready():

    # prints in command line 
    print("the bot is online!")
    # fetching the general channel 
    general = bot.get_channel(818183101007659072)
    # sends in general channel
    await general.send("Hello, Discord! , i am your assistant")

# similarly we also have on_message event
@bot.event
async def on_message(message):
    # if someone types "Hello Bot" in general channel Bot will send Hello {username}
    if message.content == "Hello Bot":
        general = bot.get_channel(id)
        user = message.author
        # print(type(user))
        await general.send(f"Hello, {user}")

    # if someone requests a joke by typing "!joke" bot will send a joke 
    if message.content == "!joke":
        joke = getJoke()
        await message.channel.send(joke)

# run the bot server by passing the token in the string 
bot.run("Token")
