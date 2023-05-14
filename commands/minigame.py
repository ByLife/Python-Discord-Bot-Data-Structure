import random
from discord.ext import commands

class MiniGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guess(self, ctx):
        """Jeu de devinette"""
        number = random.randint(1, 10)
        await ctx.send("Je pense à un nombre entre 1 et 10. Devinez quel est ce nombre !")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit()

        try:
            guess = await self.bot.wait_for("message", check=check, timeout=10)
            guess = int(guess.content)

            if guess == number:
                await ctx.send("Félicitations ! Vous avez deviné le bon nombre.")
            else:
                await ctx.send(f"Dommage, le nombre que je pensais était {number}. Essayez encore !")
        except TimeoutError:
            await ctx.send("Désolé, vous avez mis trop de temps pour deviner.")
        except ValueError:
            await ctx.send("Veuillez entrer un nombre valide.")
    
    @commands.command()
    async def rps(self, ctx, choice):
        """Joue à pierre-feuille-ciseaux contre le bot"""
        choices = ["rock", "paper", "scissors"]

        if choice == "":
            await ctx.send("Veuillez choisir entre 'rock', 'paper' ou 'scissors'.")
            return

        if choice not in choices:
            await ctx.send("Veuillez choisir entre 'rock', 'paper' ou 'scissors'.")
            return

        bot_choice = random.choice(choices)

        if choice == bot_choice:
            result = "C'est une égalité !"
        elif (
            (choice == "rock" and bot_choice == "scissors")
            or (choice == "paper" and bot_choice == "rock")
            or (choice == "scissors" and bot_choice == "paper")
        ):
            result = "Vous avez gagné !"
        else:
            result = "Vous avez perdu !"

        await ctx.send(f"Vous avez choisi '{choice}', le bot a choisi '{bot_choice}'. {result}")

def setup(bot):
    return bot.add_cog(MiniGame(bot))