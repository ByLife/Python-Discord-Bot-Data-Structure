import random
from discord.ext import commands

class QuotesCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Quotes = []

    @commands.command()
    async def add_quote(self, ctx, *, citation):
        """Ajoute une citation à la collection"""
        self.Quotes.append(citation)
        await ctx.send("Citation ajoutée !")

    @commands.command()
    async def random_quote(self, ctx):
        """Récupère une citation aléatoire de la collection"""
        if not self.Quotes:
            await ctx.send("Il n'y a aucune citation dans la collection.")
        else:
            citation_aleatoire = random.choice(self.Quotes)
            await ctx.send(f"Citation aléatoire : {citation_aleatoire}")

def setup(bot):
    return bot.add_cog(QuotesCommand(bot))