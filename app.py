# Built-In Libraries/Modules/Packages
from os import listdir
import traceback

# Third Party Libraries/Modules/Packages
from discord import ClientException, Intents
from discord.ext import commands

# User Defined Libraries/Modules/Packages
from cogs.utils.settings import Settings

intents = Intents.all()

# Initialsing bot with the prefix as `!` and 
# removing the default Help Command
bot = commands.Bot(
    command_prefix = "!",
    help_command = None,
    intents = intents
)

# To import and Load all Modules
def loadTheCogs(bot):
    cogs_dir = "cogs"
    # Getting all the python files present in `cogs` to a List
    pythonFiles = [File for File in listdir(cogs_dir) if File.endswith(".py")]

    for File in pythonFiles:
        extension = File.replace('.py', '')
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except (ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

if __name__ == "__main__":
    loadTheCogs(bot)
    bot.run(Settings().SECRETS['DISCORD_TOKEN'])
