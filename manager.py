from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

from discord.ext import commands

class Manager(commands.Cog):
    """Manage the bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Tudo pronto! Conectado como {self.bot.user}')

    @commands.Cog.listener()
    async def on_message(self, message): # getting messages

        if message.author == self.bot.user: # verifying if the message are from himself
            return

        if 'palavrão' in message.content: # verify if the message have a bad word

            await message.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários!')

            await message.delete() # delete the message if have bad word

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send('É obrigatorio enviar todos os argumentos! Digite .help para ficar informado.')
        elif isinstance(error, CommandNotFound):
            await ctx.send('O comando não existe! Digite .help para ficar informado.')
        else:
            raise error

def setup(bot):

    bot.add_cog(Manager(bot))
