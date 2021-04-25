async def joinVc(ctx):
    if ctx.message.author.voice != None:
        await ctx.message.author.voice.channel.connect()
    else:
        await ctx.send("You are not connected to a VC")
    return

async def leaveVc(ctx):
    if ctx.voice_client != None:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I'm not connected to a VC :eyes:")
    return