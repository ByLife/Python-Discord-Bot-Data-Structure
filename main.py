import os
import discord
from discord.ext import commands

from assets.linked_list import LinkedList
from assets.linked_list import Node
from commands.help import Help

intents = discord.Intents.all()

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.history = {}
        self.access_queue = LinkedList()
        self.tree_root = None
        self.tree_current_node = None

    async def check_access(self, ctx):
        if not self.access_queue.head:
            await ctx.send(f"{ctx.author.mention}, vous n'avez pas accès à l'historique actuellement.")
            return False

        current = self.access_queue.head
        found = False
        while current:
            if current.data == ctx.author.id:
                found = True
                break
            current = current.next_node

        if not found:
            await ctx.send(f"{ctx.author.mention}, vous n'avez pas accès à l'historique actuellement.")
            return False
        return True

    def create_tree(self):
        # Créer l'arbre des questions
        bot_node = Node("Avez-vous besoin d'aide avec le bot ?")
        django_node = Node("Avez-vous besoin d'aide avec Django ?")

        creator_node = Node("Le créateur de ce bot est Léo HAIDAR. Fin de la discussion. Merci ! Tapez !reset pour recommencer.")
        javascript_node = Node("Avez-vous besoin d'aide avec JavaScript ? ( Le meilleur langage de programmation )")

        javascript_node.yes_node = Node("Votre besoin est JavaScript, le meilleur langage de programmation, pas comme Python. Fin de la discussion. Merci ! Tapez !reset pour recommencer.")
        javascript_node.no_node = Node("Vous voulez alors peut-être saovir qui est le créateur de ce bot ?", yes_node=creator_node, no_node=Node("Et bien alors je ne peux pas vous aider. Merci ! Tapez !reset pour recommencer."))

        

        python_node = Node("Besoin d'aide en Python ?", yes_node=django_node, no_node=javascript_node)

        bot_node.yes_node = Node("Votre besoin est le bot, voulez-vous toutes les commandes possible de faire?")
        bot_node.no_node = python_node
        

        django_node.yes_node = Node("Votre besoin est Django, le pire framework de Python. Fin de la discussion. Merci ! Tapez !reset pour recommencer.")
        django_node.no_node = Node("Et bien alors je ne peux pas vous aider. Merci ! Tapez !reset pour recommencer.")



        self.tree_root = Node("Avez-vous besoin d'aide ?", yes_node=bot_node, no_node=python_node)

        python_node.yes_node = django_node
        python_node.no_node = javascript_node

        self.tree_current_node = self.tree_root

    def reset_tree(self):
        # Réinitialiser l'arbre et revenir au nœud racine
        self.tree_current_node = self.tree_root

    def traverse_tree(self, answer):
        # Parcourir l'arbre en fonction de la réponse de l'utilisateur
        if answer.lower() == "oui" and self.tree_current_node.yes_node:
            self.tree_current_node = self.tree_current_node.yes_node
        elif answer.lower() == "non" and self.tree_current_node.no_node:
            self.tree_current_node = self.tree_current_node.no_node
        else:
            return "Je ne peux pas répondre à votre question."

        if self.tree_current_node.yes_node is None and self.tree_current_node.no_node is None:
            # Nœud terminal atteint
            return "Votre besoin est {}".format(self.tree_current_node.question)
        
        return self.tree_current_node.question


bot = Bot(command_prefix="!", intents=intents)
bot.help_command = Help()

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"commands.{filename[:-3]}")


if __name__ == "__main__":
    with open("token.txt", "r") as token_file:
        TOKEN = token_file.read().strip()

    bot.run(TOKEN)