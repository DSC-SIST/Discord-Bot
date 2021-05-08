# Third Party Libraries/Modules/Packages
from discord.ext import commands


class Chat(commands.Cog):
    """
    Extending the commands.Cog class for Chat based commands and events.
    """

    def __init__(self, bot):
        '''
        The default constructor for the class: Chat
        '''
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.emoji.name == '\N{PUSHPIN}' and payload.user_id != self.bot.user.id:
            # To prevent errors in case of lack of permission or HTTP Exception
            try:
                channel=self.bot.get_channel(payload.channel_id)
                message=await channel.fetch_message(payload.message_id)
                await message.pin(reason="Requested by "+str(payload.user_id))
            except:
                pass
        return
        
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.emoji.name == '\N{PUSHPIN}' and payload.user_id != self.bot.user.id:
            try:
               channel=self.bot.get_channel(payload.channel_id)
               message=await channel.fetch_message(payload.message_id)
               await message.unpin(reason="Requested by "+str(payload.user_id))
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
                await after.remove_reaction("📌", self.bot.user)
            except:
                pass
        return


def setup(bot):
    '''
    Following the docs for creating cogs
    '''
    bot.add_cog(Chat(bot))
