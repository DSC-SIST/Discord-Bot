from discord.ext import commands

# Extending the commands.Cog class
class Help(commands.Cog):

    # The constructor 
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        name = 'help',
        invoke_without_command = True
    )
    async def help(self, ctx):
        await ctx.channel.send('Base help command. Sub commands: Misc, Fun, Music')

    @help.command(name = 'misc')
    async def misc_subcommand(self, ctx):
        await ctx.channel.send('Misc Subcommand from help!')

    @help.command(name = 'fun')
    @commands.has_any_role('admin')
    async def fun_subcommand(self, ctx):
        await ctx.channel.send('Fun Subcommand from help!')

    @help.command(name = 'music')
    async def music_subcommand(self, ctx, arg1):
        await ctx.channel.send('Music Subcommand from help!')

# Following the docs for creating cogs
def setup(bot):
    bot.add_cog(Help(bot))
