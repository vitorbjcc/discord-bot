from discord.ext import commands


class Crypto(commands.Cog):
    """Works with Cryptocurrency"""
    
    def __init__(self, bot):
        self.bot = bot

def setup(bot):

    bot.add_cog(Crypto(bot))
