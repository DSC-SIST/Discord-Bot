from discord.ext import commands

class Chat(commands.Cog):
    ''' For Chat based commands and events '''	
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == '📌' and user.id != self.bot.user.id:
        # To prevent errors in case of lack of permission or HTTP Exception
            try:
                await reaction.message.pin(reason='Requested by '+ str(user.id))
            except:
                pass
        return

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.author.id == self.bot.user.id:
            return
        if not before.pinned and after.pinned:
            # To prevent bot from reacting to already reacted messages
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
                await after.remove_reaction("📌",self.bot.user)
            except:
                pass
        return

def setup(bot):
    bot.add_cog(Chat(bot))
    
