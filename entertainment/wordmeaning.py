import requests
from discord import Embed, Color

async def getmeaning(ctx):
    word=ctx.message.content.split(" ")[1]
    data=eval(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/"+str(word)).content.decode())
    if type(data)=="dict":
        ctx.send("Ooops. I could not find the meaning. Maybe try searching somewhere on web or checking the spelling??")
        return
    embed=Embed(title=str(word).capitalize(), color=Color.blue())
    data=data[0]
    try:
        embed.add_field(name="Pronounciation", value=data["phonetics"][0]["text"], inline=True)
        embed.add_field(name="Hear it!", value=data["phonetics"][0]["audio"], inline=True)
        embed.add_field(name="** **", value="** **", inline=False)
    except:
        pass
    for i in data["meanings"]:
        embed.add_field(name=str(i["partOfSpeech"]).capitalize(), value=i["definitions"][0]["definition"], inline=False)
        try:
            synstr=''
            for x in i["definitions"][0]["synonyms"]:
                synstr+=str(x).capitalize()
                synstr+=", "
            synstr=synstr.strip()
            synstr=synstr.strip(",")
            embed.add_field(name="Synonyms", value=synstr, inline=False)
        except:
            pass
        embed.add_field(name="** **", value="** **", inline=False)
    await ctx.send(embed=embed)
    return