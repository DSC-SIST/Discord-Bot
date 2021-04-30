from discord.ext import commands

# Extending the commands.Cog class
class Administrator(commands.Cog):

    # The constructor 
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name = 'banuser',
        aliases = ['ban']
    )
    @commands.has_any_role('admin', 'Festus')
    async def ban_user_command(self, ctx, username):
        await ctx.channel.send("Banned {}.".format(username))

# Following the docs for creating cogs
def setup(bot):
    bot.add_cog(Administrator(bot))
