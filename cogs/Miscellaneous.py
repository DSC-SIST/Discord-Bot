# Third Party Libraries/Modules/Packages
from discord import Embed, Color
from discord.ext import commands

# User Defined Libraries/Modules/Packages
from .utils.misc import checklinkfunc
from .utils.misc import getJoke


class MiscCommands(commands.Cog):
    '''
    Extending the commands.Cog class for miscellaneous commands.
    '''

    def __init__(self, bot):
        '''
        The default constructor for MiscCommands class.
        '''
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
        try:
            setup = str(joketosend['setup'])
            punchline = str(joketosend['punchline'])
            await ctx.send(f"{setup}\n{punchline}")
        except:
            pass


def setup(bot):
    '''
    Following the docs for creating cogs
    '''
    bot.add_cog(MiscCommands(bot))
