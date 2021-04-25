import discord
from discord.ext import commands
import os

#importing features as modules
from entertainment.wordmeaning import getmeaning
from entertainment.saynoice import saynoice
from entertainment.saypong import saypong

from entertainment.music.lyrics import findlyric
from entertainment.music.joinAndLeaveVc import joinVc, leaveVc
from entertainment.music.songControls import play, pause, resume, stop, loop, queue, current, skip, vol, remove

from botactions.addPinEmoji import addpin
from botactions.reactToPinEmoji import reactToPin

from tools.linkchecker import checklink
from tools.exportChat import exportChat
from tools.userInfo import userinfo
from tools.serverStats import serverstats

token=token=os.getenv("BOT_TOKEN")
prefix="$" #prefix=os.getenv("PREFIX")
intent=discord.Intents.all()

bot=commands.Bot(command_prefix=prefix, intents=intent)

@bot.command(name="meaning", aliases=['whatdoesitmean','define'], brief='Returns the meaning of the word', help="Says the dictionary meaning of the given word")
async def _meaning(ctx):
    await getmeaning(ctx)
    return

@bot.command(name="noice", aliases=["nice"], brief="Says \'noice\'.", help="Says noice!")
async def _noice(ctx):
    await saynoice(ctx)
    return

@bot.command(name="ping", breif="Says \'pong\'", help="Says pong!")
async def _ping(ctx):
    await saypong(ctx)
    return

@bot.command(name="lyrics", aliases=["lyric","findl"], brief="Finds and returns song lyrics", help="Finds lyric for song specified")
async def _lyrics(ctx):
    await findlyric(ctx)
    return

@bot.command(name="checklink", aliases=["issafe","caniuse"], brief="Check if given link is safe or not", help="Checks if given link is safe or not")
async def _checklink(ctx):
    await checklink(ctx)
    return

@bot.command(name="savechat", aliases=["exportchat"], brief="Exports chat (last 500 messages) into a file", help="Exports chat (last 500 messages) into a file")
async def _save(ctx):
    await exportChat(ctx)
    return

# Music Commands

@bot.command(name="join", aliases=['j'], brief="Joins the VC", help="Joins the VC the user is in")
async def _join(ctx):
    await joinVc(ctx)
    return

@bot.command(name="leave", aliases=['dc','disconnect'], brief="Leaves the VC", help="Leaves the VC")
async def _leave(ctx):
    await leaveVc(ctx)
    return

@bot.command(name="play", aliases=['p'], brief="Plays a song", help="Plays a song")
async def _play(ctx):
    await play(ctx)
    return

@bot.command(name="pause", aliases=["waitforme"], brief="Pauses a song", help="Pauses song")
async def _pause(ctx):
    await pause(ctx)
    return

@bot.command(name="resume", aliases=["continue"], brief="Continues playing", help="Continues the paused song")
async def _resume(ctx):
    await resume(ctx)
    return

@bot.command(name="stop", brief="Stops playing", help="Stops playing.")
async def _stop(ctx):
    await stop(ctx)
    return

@bot.command(name="loop", brief="Loops the current song", help="Loops the current song infinitely")
async def _loop(ctx):
    await loop(ctx)
    return

@bot.command(name="queue", aliases=['q'], brief="Displays the queue", help="Displays the queue")
async def _queue(ctx):
    await queue(ctx)
    return

@bot.command(name="skip", aliases=['next'], brief="Skips song", help="Skips the current song")
async def _skip(ctx):
    await skip(ctx)
    return

@bot.command(name="current", aliases=["np", "playing"], brief="Displays the current song", help="Displays the current song")
async def _current(ctx):
    await current(ctx)
    return

@bot.command(name="volume", aliases=["vol"], brief="To change volume", help="To change volume")
async def _vol(ctx):
    await vol(ctx)
    return

@bot.command(name="remove", aliases=["rm", "del"], brief="Removes song from queue", help="Removes song from queue")
async def _remove(ctx):
    await remove(ctx)
    return

# Music commands ends

@bot.command(name="userinfo", aliases=["uinf"], brief="Get's a user's info", help="Get's a user's info")
async def _userinfo(ctx):
    await userinfo(ctx)
    return

@bot.command(name="serverstats", aliases=["serverinfo"], brief="Get's servers stats", help="Get's servers stats")
async def _serverstats(ctx):
    await serverstats(ctx)
    return

@bot.event
async def on_reaction_add(reaction, user):
    await addpin(reaction, user, bot)
    return

@bot.event
async def on_message_edit(before,after):
    await reactToPin(before, after, bot)
    return

bot.run(token)
