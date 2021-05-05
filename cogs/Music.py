from discord.ext import commands

# Extending the commands.Cog class
class Music(commands.Cog):

    # The constructor 
    def __init__(self, bot):
        self.bot = bot

# Following the docs for creating cogs
def setup(bot):
    bot.add_cog(Music(bot))
