import lyricsgenius as Genius
import os
from discord import Embed, Color

gtoken=os.getenv("GENIUSTOKEN")
api=Genius.Genius(gtoken)

async def findlyric(ctx):
    if len(ctx.message.content.split(" "))>2:
        song=api.search_song(' '.join(ctx.message.content.split(" ")[1:]))
        l=song.lyrics
        if len(l)>1000:
            lst=[]
            splitFlag=True
            n=0
            while n<len(l):
                lst.append(l[n:n+1000])
                n=n+1000
        else:
            splitFlag=False
        embed=Embed(title=song.title, description=song.artist, color=0x9b9ff7)
        embed.set_thumbnail(url=song.song_art_image_thumbnail_url)
        if splitFlag==False:
            embed.add_field(name="** **", value=l, inline=False)
        else:
            for i in lst:
                embed.add_field(name="** **",value=i, inline=False)
        embed.set_footer(text="Fetched using Genius")
        await ctx.send(embed=embed)