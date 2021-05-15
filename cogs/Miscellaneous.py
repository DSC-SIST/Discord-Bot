# Third Party Libraries/Modules/Packages
from discord.ext import commands

# User Defined Libraries/Modules/Packages
from .utils.misc import checklinkfunc, getJoke

# Extending the commands.Cog class


class MiscCommands(commands.Cog):

    # The constructor
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='hello',
        aliases=['h', 'he', 'hl']
    )
    async def hello_command(self, ctx):
        await ctx.channel.send('Hello there!')

    @commands.command(
        name='roll',
        aliases=['rolldice', 'rdice']
    )
    async def roll_dice_command(self, ctx):
        await ctx.channel.send('Roll Dice command works!')

    @commands.command(
        name='assignrole',
        aliases=['addrole']
    )
    async def add_role_command(self, ctx, arg1):
        await ctx.channel.send('Adding Role ' + arg1)

    @commands.command(
        name='removerole',
        aliases=['delrole']
    )
    async def hello_command(self, ctx):
        await ctx.channel.send('Removing Role!')

    @commands.command(
        name="checklink",
        aliases=["link", "check"]
    )
    async def link_check_func(self, ctx, link):
        msgtosend = checklinkfunc(link)
        await ctx.channel.send(msgtosend)

    @commands.command(
        name="getjoke",
        aliases=["joke"]
    )
    async def get_joke(self, ctx):
        joketosend = getJoke()
        setup = str(joketosend['setup'])
        punchline = str(joketosend['punchline'])
        await ctx.send(f"{setup}\n{punchline}")

# Following the docs for creating cogs
def setup(bot):
    bot.add_cog(MiscCommands(bot))
