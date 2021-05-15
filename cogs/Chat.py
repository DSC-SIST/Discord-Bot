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
                channel = self.bot.get_channel(payload.channel_id)
                message = await channel.fetch_message(payload.message_id)
                await message.pin(reason="Requested by "+str(payload.user_id))
            except:
                pass
        return

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.emoji.name == '\N{PUSHPIN}' and payload.user_id != self.bot.user.id:
            try:
                channel = self.bot.get_channel(payload.channel_id)
                message = await channel.fetch_message(payload.message_id)
                await message.unpin(reason="Requested by "+str(payload.user_id))
            except:
                pass
        return

    @commands.Cog.listener()
    async def on_raw_message_edit(self, payload):
        message = payload.cached_message
        if not message:
            channel = self.bot.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
        
        if payload.data['pinned']:
            if payload.data['author']['id']!=self.bot.user.id:
                await message.add_reaction("📌")
                return
        if not(payload.data['pinned']):
            try:
                await message.remove_reaction("📌",self.bot.user)
            except:
                pass
        return

def setup(bot):
    '''
    Following the docs for creating cogs
    '''
    bot.add_cog(Chat(bot))
