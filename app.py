# import discord package 
# pip install discord
import discord

# this is our bot 
bot = discord.Client()

# event listeners 
@bot.event  
# defining function for on_ready function
# on_ready is predefined function under discord package 
async def on_ready():

    # prints in command line 
    print("the bot is online!")
    
    # fetching the general channel 
    general = bot.get_channel(818183101007659072)

    await general.send("Hello, Discord! , i am your assistant")

# similarly we also have on_message event
@bot.event
async def on_message(message):
    if message.content == "Hello AlexBot":
        general = bot.get_channel(id)
        user = message.author
        # print(type(user))
        await general.send(f"Hello, {user}")



# run the bot server by passing the token in the string 
bot.run("Token")