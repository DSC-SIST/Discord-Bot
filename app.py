# import discord package 
# pip install discord
import discord
from dotenv import load_dotenv
import os

load_dotenv()
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
bot = discord.Client(intents=intents)

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

#To add pin message on reaction
@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji=='📌' and user.id!=bot.user.id:
        try: # To prevent errors in case of lack of permission or HTTP Exception
            await reaction.message.pin(reason='Requested by '+str(user.id))
        except:
            pass
    return

#To monitor and add/remove reaction to pins
@bot.event
async def on_message_edit(before,after):
    if after.author.id == bot.user.id:
        return
    if not before.pinned and after.pinned:
        #To prevent bot from reacting to already reacted messages
        for i in after.reactions:
            if i.emoji=='📌':
                return
        try: # To prevent errors in case of lack of permission or HTTP Exception
            await after.add_reaction("📌")
        except:
            pass
    if before.pinned and not after.pinned:
        try: # To prevent errors in case of lack of permission or HTTP Exception
            await after.remove_reaction("📌",bot.user)
        except:
            pass
    return

@bot.event
async def on_member_join(member):
    guild_id = int(os.getenv('GUILD_ID'))
    channel_id = int(os.getenv('WELCOME_CHANNEL_ID'))
    guild = bot.get_guild(guild_id)
    channel = guild.get_channel(channel_id)
    await channel.send(f"Welcome to the server {member.mention} ! :partying_face:")
    await member.send(f"Welcome to the {guild.name} server, {member.name}! :partying_face:")

bot.run(os.getenv('TOKEN'))
