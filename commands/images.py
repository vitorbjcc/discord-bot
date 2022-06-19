from discord.ext import commands

import discord

class Images(commands.Cog):
    """Works with images"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='foto', help='Envia uma embed (argumento opcional)')
    async def get_random_image(self, ctx, url_image='https://picsum.photos/1920/1080'): # give a embed with photos
        
        embed = discord.Embed( # creating embed
            title = 'Resultado da busca de imagem',
            description = 'A busca é totalmente aleatória',
            color = 0x32cadb
        )

        embed.add_field(name='API', value='Usamos a API do https://picsum.photos/1920/1080')

        embed.add_field(name='Parâmetros', value='{largura}/{altura}')

        embed.add_field(name='Créditos', value='Aprendi com a ByLearn!', inline=False)

        embed.set_image(url=url_image)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.set_footer(text='By cuphead', icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed) # send embed

    @commands.command(name='sainever', help='Não vou dizer nada! Este comando não da o token do bot!') # new command
    async def troll(self, ctx):
        embed = discord.Embed(
            title = 'Never Gonna Give You Up',
            description = 'TROLLED',
            color = 0x32cadb
        )

        embed.add_field(name='TROLLED', value='BE CAREFULL ' + ctx.author.user.name)

        embed.add_field(name='SONG', value='THIS SONG IS VERY GOOD')

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.set_footer(text='By Cuphead', icon_url=self.bot.user.avatar_url)

        embed.set_image(url='https://www.tenhomaisdiscosqueamigos.com/wp-content/uploads/2021/02/rickroll-hd.jpg')

        await ctx.send(embed=embed)

def setup(bot):

    bot.add_cog(Images(bot))
