import os
import json
from discord.ext import commands

class HistoryCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.history_folder = "history" 
        self.history = {}

        for file_name in os.listdir(self.history_folder):
            user_id = file_name.split(".")[0]
            user_history = self.load_user_history(user_id)
            self.history[user_id] = user_history
            print(self.history)


    def load_user_history(self, user_id):
        file_name = f"{user_id}.json"
        file_path = os.path.join(self.history_folder, file_name)
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_user_history(self, user_id, history):
        os.makedirs(self.history_folder, exist_ok=True)
        file_path = os.path.join(self.history_folder, f"{user_id}.json")
        with open(file_path, "w") as file:
            json.dump(history, file, indent=4)

    @commands.Cog.listener()
    async def on_ready(self):
        for file_name in os.listdir(self.history_folder):
            user_id = file_name.split(".")[0]
            user_history = self.load_user_history(user_id)
            self.history[user_id] = user_history
            print(self.history)

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        """Sauvegarde la commande dans l'historique"""
        if ctx.author.bot or ctx.command.name == "history":
            return

        user_id = str(ctx.author.id)
        user_history = self.history.get(user_id)
        if user_history is None:
            user_history = []
            self.history[user_id] = user_history

        user_history.append(ctx.message.content)
        self.save_user_history(user_id, user_history)

    @commands.command()
    async def last_command(self, ctx):
        """Affiche la dernière commande entrée par l'utilisateur"""
        if not await self.bot.check_access(ctx):
            return
        user_id = str(ctx.author.id)
        user_history = self.history.get(user_id)

        if user_history is not None and len(user_history) > 1:
            last_command = user_history[-2]
            await ctx.send(f"@{ctx.author}, la dernière commande rentrée était : {last_command}")
        else:
            await ctx.send(f"@{ctx.author}, vous n'avez pas d'historique")

    @commands.command()
    async def clear_history(self, ctx):
        """Supprime l'historique de l'utilisateur"""
        if not await self.bot.check_access(ctx):
            return

        user_id = str(ctx.author.id)
        user_history = self.history.get(user_id)
        if user_history is not None:
            user_history.clear()
            self.save_user_history(user_id, user_history)

            await ctx.send(f"{ctx.author.mention}, votre historique a été clear !")
        else:
            await ctx.send(f"{ctx.author.mention}, il n'y a pas d'historique pour vous.")

    @commands.command(name="history")
    async def _history(self, ctx):
        """Affiche l'historique de l'utilisateur"""
        user_id = str(ctx.author.id)
        user_history = self.history.get(user_id)
        if user_history is None or len(user_history) == 0:
            await ctx.send(f"{ctx.author.mention}, il n'y a pas d'historique pour vous.")
        else:
            history_str = "\n".join(user_history)
            await ctx.send(f"Historique des commandes pour {ctx.author.mention}:\n```\n{history_str}\n```")

def setup(bot):
    return bot.add_cog(HistoryCommands(bot))
