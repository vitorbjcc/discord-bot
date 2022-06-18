from discord.ext import commands


class Smarts(commands.Cog):
    """A lot of Smart Commands"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='calcular', help='Calcula uma operação matemática e mostra o resultado') # add a command
    async def calculate_expression(self, ctx, *expression):

        expression = ''.join(expression) # add letters from expression arg

        response = eval(expression) # math func eval

        await ctx.send(f'A resposta é : {str(response)}') # send response

def setup(bot):

    bot.add_cog(Smarts(bot))
