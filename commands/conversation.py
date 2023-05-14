import random
from discord.ext import commands

class ConversationCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def conversation(self, ctx):
        """Initialise la discussion"""
        self.bot.create_tree()
        await ctx.send("Bonjour ! Je suis là pour vous aider. Répondez aux questions en utilisant !answer oui ou !answer non.")
        await ctx.send(self.bot.tree_current_node.question)

    @commands.command()
    async def reset(self, ctx):
        """Réinitialise la discussion"""
        self.bot.reset_tree()
        await ctx.send("La discussion a été réinitialisée.")
        await ctx.send(self.bot.tree_current_node.question)

    @commands.command()
    async def speak(self, ctx, topic):
        """Répond à une question"""
        if topic == "":
            await ctx.send("Veuillez entrer un sujet.")
            return

        if self.bot.tree_current_node:
            result = self.bot.traverse_tree(topic)
            if result:
                await ctx.send(result)
            else:
                await ctx.send("Je ne peux pas répondre à votre question.")
        else:
            await ctx.send("La discussion n'a pas encore été initialisée. Utilisez la commande '!help' pour commencer.")

    @commands.command()
    async def answer(self, ctx, response):
        """Répond à une question"""
        if self.bot.tree_current_node:
            result = self.bot.traverse_tree(response)
            await ctx.send(result)
        else:
            await ctx.send("La discussion n'a pas encore été initialisée. Utilisez la commande '!help' pour commencer.")


def setup(bot):
    return bot.add_cog(ConversationCommands(bot))