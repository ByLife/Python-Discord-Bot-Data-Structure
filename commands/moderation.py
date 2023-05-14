from discord.ext import commands

class ModerationCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """Efface un certain nombre de messages dans un salon."""
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{amount} messages ont été effacés.", delete_after=5)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        """Expulse un membre du serveur."""
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} a été expulsé du serveur.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        """Banni un membre du serveur."""
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} a été banni du serveur.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        """Débanni un membre du serveur."""
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            if user.name == member:
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} a été débanni du serveur.")
                return

        await ctx.send(f"{member} n'est pas dans la liste des bannis du serveur.")

def setup(bot):
    return bot.add_cog(ModerationCommands(bot))