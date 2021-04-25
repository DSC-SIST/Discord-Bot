import random
from discord import File
import os
async def exportChat(ctx):
    messages=await ctx.message.channel.history(oldest_first=True).flatten()
    tfname=str(random.randint(1000,5000))+"MessageExport"+str(ctx.message.channel.name)+".txt"
    path_=os.getcwd()+"/"
    tfile=open(tfname,'w')
    for message in messages:
        tstr="["+str(message.author.name)+"]\t"+str(message.content)+"\t["+str(message.created_at)+"]"
        tstr="\n\n"
        tfile.write(tstr)
    tfile.close()
    fullpath=path_+tfname
    await ctx.send("Message export is ready!! ", file=File(fullpath))
    os.remove(fullpath)
    return