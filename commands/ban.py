@bot.command()
@commands.has_permissions(ban_members=True, kick_members=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("**Please specify a member**")
        return
    await member.ban()
    await ctx.send(f"{member.mention} Was banned by {ctx.author.mention}, [{reason}]")
# This displays an error if the user doesn't have the required permmissions (caso a pessoa tente usar n vai ao menos que tenha permissão)
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("**Você não tem permissão para banir membros**")