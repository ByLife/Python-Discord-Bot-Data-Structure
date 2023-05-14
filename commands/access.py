from discord.ext import commands

class Access(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def request_access(self, ctx):
        """Ajoute l'enregistrement des commandes de l'utilisateur et ajoute l'accès à last_command"""
        if ctx.author.id not in self.bot.access_queue.get_all():
            self.bot.access_queue.append(ctx.author.id)
            await ctx.send(f"{ctx.author.mention}, vous avez été ajouté dans la whitelist")
        else:
            await ctx.send(f"{ctx.author.mention}, vous avez déjâ été ajouté dans la whitelist")


    @commands.command()
    async def release_access(self, ctx):
        """Retire l'enregistrement des commandes de l'utilisateur et retire l'accès à last_command"""
        if self.bot.access_queue.head and self.bot.access_queue.head.data == ctx.author.id:
            self.bot.access_queue.head = self.bot.access_queue.head.next_node
            await ctx.send(f"{ctx.author.mention}, vous avez été retiré de la whitelist")
        else:
            await ctx.send(f"{ctx.author.mention}, vous n'avez pas accès à cette commande")
    

def setup(bot):
    return bot.add_cog(Access(bot))