from discord.ext import commands


class Reactions(commands.Cog):
    """Works with reactions"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user): # reaction event
        print(reaction.emoji)
        
        if reaction.emoji == '👍': # condition
            role = user.guild.get_role(987407926312452226)

            await user.add_roles(role)

        elif reaction.emoji == '💩': # other condition
            role = user.guild.get_role(987408148136591360)

            await user.add_roles(role)

def setup(bot):

    bot.add_cog(Reactions(bot))
