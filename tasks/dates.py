from discord.ext import commands, tasks

import datetime

class Dates(commands.Cog):
    """Work with dates"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(hours=1) # add a task
    async def current_time(self):

        now = datetime.datetime.now() # getting date

        now = now.strftime('%d/%m/%Y às %H:%M:%S') # formating the date

        channel = self.bot.get_channel(924326137222537256) # get a discord channel

        await channel.send(f'Data atual: {now}') # send date formated on a channel

def setup(bot):

    bot.add_cog(Dates(bot))
