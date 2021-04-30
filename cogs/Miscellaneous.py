from discord.ext import commands

# Extending the commands.Cog class
class MiscCommands(commands.Cog):

    # The constructor 
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name = 'hello',
        aliases = ['h', 'he', 'hl']
    )
    async def hello_command(self, ctx):
        await ctx.channel.send('Hello there!')

    @commands.command(
        name = 'roll',
        aliases = ['rolldice', 'rdice']
    )
    async def roll_dice_command(self, ctx):
        await ctx.channel.send('Roll Dice command works!')

    @commands.command(
        name = 'assignrole',
        aliases = ['addrole']
    )
    async def add_role_command(self, ctx, arg1):
        await ctx.channel.send('Adding Role ' + arg1)

    @commands.command(
        name = 'removerole',
        aliases = ['delrole']
    )
    async def hello_command(self, ctx):
        await ctx.channel.send('Removing Role!')

# Following the docs for creating cogs
def setup(bot):
    bot.add_cog(MiscCommands(bot))
