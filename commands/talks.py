from discord.ext import commands

import discord

class Talks(commands.Cog):
    """Talks with user"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', help='Envia um Pong! (não requer argumentos)') # simple command to greet the user
    async def send_pong(self, ctx):

        await ctx.send('Pong!') # bot sends the variable named with response

    @commands.command(name='segredo', help='Envia um segredinho...') # its nothing...
    async def secret(self, ctx):
        try:
            await ctx.author.send('ByLearn learn me how to create this bot!')

            await ctx.author.send('Thank you ByLearn!')

        except discord.errors.Forbidden:

            await ctx.send(f'{ctx.author.name}, seu PV não está aberto! 👀')

    @commands.command(name='say', help='Depois do ctx o bot ira dizer tudo oque foi digitado') # say command
    async def _say_(self, ctx, *, arg):
        
        await ctx.send(arg)

def setup(bot):

    bot.add_cog(Talks(bot))
