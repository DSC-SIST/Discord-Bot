# Import required modules
import discord
from urllib import request
import json
from pysafebrowsing import SafeBrowsing

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

# Func to check if a link is malicious or not
def linkcheck(msg):
    s = SafeBrowsing('API_KEY') # Access the API
    link=msg[7:len(msg)+1] # Getting the link from the message
    r = s.lookup_urls([link]) # Check if the link is safe or not
    # Return the result
    if r[link]["malicious"]==False:
        return link+" **is not malicious**"
    elif r[link]["malicious"]==True:
        return link+" **is malicious**"
    else:
        return "Something's is wrong"

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

    # Example command: !check https://www.wolframalpha.com/%22%7D
    # Example result: https://www.wolframalpha.com/%22%7D **is not malicious** 
    if message.content.startswith("!check") or message.content.startswith("!Check"):
        await message.channel.send(linkcheck(message.content))

# run the bot server by passing the token in the string 
bot.run("Token")