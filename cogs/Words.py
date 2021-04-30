# Built-In Libraries/Modules/Packages
import os

# Third Party Libraries/Modules/Packages
from discord import Embed, Color
from discord.ext import commands
import requests

# User Defined Libraries/Modules/Packages
from .utils.settings import Settings

# Extending the commands.Cog class
class Words(commands.Cog):

    # The constructor 
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name = 'meaning',
        aliases = ['what', 'def', 'define']
    )
    async def getmeaning(self, ctx, word):
        DICTONARY_API = Settings().SECRETS['DICTIONARY_API']
        data = eval(requests.get(DICTONARY_API + str(word)).content.decode())

        if type(data) == "dict":
            message = "Ooops. I could not find the meaning." 
            message += "Maybe try searching somewhere on web"
            message += " or checking the spelling??"
            ctx.send(message)
            return

        embed = Embed(
            title = str(word).capitalize(),
            color = Color.blue()
        )
        data = data[0]

        try:
            embed.add_field(
                name = "Pronounciation",
                value = data["phonetics"][0]["text"],
                inline = True
            )
            embed.add_field(
                name = "Hear it!",
                value = data["phonetics"][0]["audio"],
                inline = True
            )
        except:
            pass

        for i in data["meanings"]:
            embed.add_field(
                name = str(i["partOfSpeech"]).capitalize(),
                value = i["definitions"][0]["definition"],
                inline = False
            )
            try:
                synstr = ''
                for x in i["definitions"][0]["synonyms"]:
                    synstr += str(x).capitalize()
                    synstr += ", "

                synstr = synstr.strip()
                synstr = synstr.strip(",")
                embed.add_field(
                    name = "Synonyms",
                    value = synstr,
                    inline = False
                )
            except:
                pass

        await ctx.send(embed = embed)
        return

# Following the docs for creating cogs
def setup(bot):
    bot.add_cog(Words(bot))
