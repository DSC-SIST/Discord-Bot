async def addpin(reaction, user, bot):
    if reaction.emoji == '📌' and user.id != bot.user.id:
        # To prevent errors in case of lack of permission or HTTP Exception
        try:
            await reaction.message.pin(reason='Requested by '+ str(user.id))
        except:
            pass
    return