from bs4 import BeautifulSoup
import discord
from dotenv import load_dotenv
import fnmatch
import json
from lxml import html
from random_word import RandomWords
import requests
import re
import os
from urllib.request import Request, urlopen

load_dotenv()
client = discord.Client()
r = RandomWords()
# Return a single random word
urlin = r.get_random_word().strip().lower().replace(" ", "")

def get_word():
    while True:
        url = "https://www.lexico.com/en/definition/"
        if (len(urlin) == 0): continue

        url += urlin
        req = Request(url)

        fail = False
        for x in range(0, 10):
            if (x == 10):
                fail = True
                break

            try:
                html_page = urlopen(req)
                soup = BeautifulSoup(html_page, "lxml")
                break

            except: continue

        if (fail == True):
            print("Error 404\n\n")
            continue

        contents = soup.findAll(class_="semb")
        definitions = []
        takeaway = 0
        for f in range(len(contents)):
            body = contents[f].select(".iteration, .subsenseIteration, .ind")
            x = 1
            construct = ""
            for item in body:
                if (x % 2 == 0):
                    construct += str(item.get_text())
                    definitions.append(construct)
                    construct = ""
                else: construct += str(item.get_text()) + " - "
                x += 1
            takeaway += 1

        word_bank = []
        for item in definitions:
            if (item != ""):
                word_bank.append(item)

        return ("╔══════════════════════════════════════════════════════════════════\n║ Word: " + str(urlin) + "\n║ Item count: " + str(len(word_bank)-takeaway) + "\n╠══════════════════════════════════════════════════════════════════\n║ " + '\n║ '.join(word_bank) + "\n╚══════════════════════════════════════════════════════════════════")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$word'):
        word = get_word()
        await message.channel.send(word)

client.run(str(os.getenv('TOKEN')))