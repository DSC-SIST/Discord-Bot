from dotenv import dotenv_values

class Settings:
    """
    Abstract entity to hold the settings for the bot.
    Methods:
        getSecrets(self)
    """

    # The constructor 
    def __init__(self):
        self.SECRETS = dict(dotenv_values())


    def getSecrets(self) -> dict:
        """
        Returns the environmental variables.
        """

        return self.SECRETS
