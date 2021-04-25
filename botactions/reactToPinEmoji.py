async def reactToPin(before, after, bot):
    if after.author.id == bot.user.id:
        return
    if not before.pinned and after.pinned:
        #To prevent bot from reacting to already reacted messages
        for i in after.reactions:
            if i.emoji == '📌':
                return

        # To prevent errors in case of lack of permission or HTTP Exception
        try:
            await after.add_reaction("📌")
        except:
            pass
    if before.pinned and not after.pinned:
        # To prevent errors in case of lack of permission or HTTP Exception
        try:
            await after.remove_reaction("📌",bot.user)
        except:
            pass
    return