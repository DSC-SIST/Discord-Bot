import DiscordUtils
music = DiscordUtils.Music()

async def play(ctx):
    song_=ctx.message.content.split(" ")[1]
    player = music.get_player(guild_id=ctx.message.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(song_, search=True)
        song = await player.play()
        await ctx.send(f"Playing {song.name}")
    else:
        song = await player.queue(song_, search=True)
        await ctx.send(f"Queued {song.name}")
    return

async def pause(ctx):
    player=music.get_player(guild_id=ctx.message.guild.id)
    if not player:
        await ctx.send("Nothing is playing rn...")
        return  
    else:
        song=await player.pause()
        await ctx.send(f"Paused {song.name}")
    return

async def resume(ctx):
    player = music.get_player(guild_id=ctx.message.guild.id)
    if not player:
        await ctx.send("Nothing is paused rn...")
        return
    song = await player.resume()
    await ctx.send(f"Resumed {song.name}")
    return

async def stop(ctx):
    player = music.get_player(guild_id=ctx.message.guild.id)
    if not player:
        await ctx.send("Nothing is playing rn...")
        return
    await player.stop()
    await ctx.send("Stopped")
    return

async def loop(ctx):
    player = music.get_player(guild_id=ctx.message.guild.id)
    if not player:
        await ctx.send("Nothing is playing rn... :eyes:")
        return
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"Enabled loop for {song.name}")
    else:
        await ctx.send(f"Disabled loop for {song.name}")
    return

async def queue(ctx):
    player = music.get_player(guild_id=ctx.message.guild.id)
    if not player:
        await ctx.send("Nothing is playing rn... :eyes:")
    content = "```nim\n\n"
    content += '\n'.join([song.name for song in player.current_queue()])
    content += "\n```"
    await ctx.send(content)
    return

async def current(ctx):
    player = music.get_player(guild_id=ctx.message.guild.id)
    if not player:
        await ctx.send("Nothing is playing rn...")
        return
    song = player.now_playing()
    await ctx.send(song.name)
    return

async def skip(ctx):
    player = music.get_player(guild_id=ctx.message.guild.id)
    if not player:
        await ctx.send("Nothing is playing rn...")
        return
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Skipped from `{data[0].name}` to `{data[1].name}`")
    else:
        await ctx.send(f"Skipped {data[0].name}")
    return

async def vol(ctx):
    try:
        vol=float(ctx.message.content.split(" ")[1])
    except:
        await ctx.send("Not a valid volume!")
        return
    player = music.get_player(guild_id=ctx.message.guild.id)
    if not player:
        await ctx.send("What volume are you even trying to change? Nothing's playing rn... smh")
        return
    song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
    await ctx.send(f"Changed volume for {song.name} to {volume*100}%")
    return

async def remove(ctx):
    index=int(ctx.message.content.split(" ")[1])
    player = music.get_player(guild_id=ctx.message.guild.id)
    if not player:
        await ctx.send("Nothing is playing rn...")
        return
    song = await player.remove_from_queue(int(index))
    await ctx.send(f"Removed {song.name} from queue")
    return