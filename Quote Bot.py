import discord
from dotenv import load_dotenv
import json
import os
import requests
import DLLs

load_dotenv()
client = discord.Client()

def get_quote():
    response = requests.get(os.getenv('QUOTE_API'))
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " ~" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('pls quote'):
        quote = get_quote()
        await message.channel.send(quote)

client.run(str(os.getenv('TOKEN')))
#print(os.getenv('TOKEN'))