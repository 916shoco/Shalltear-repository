import discord
import os
from discord.ext import commands
token = os.environ.get('token')

description =  "filha do shoco"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command(name="calcular")
async def calculate_expression(ctx, *expression):
    expression = "".join(expression)

    print(expression)
  
    response = eval(expression)
    
    await ctx.send("A resposta é: " + str(response))

@bot.command()
@commands.has_permissions(ban_members=True, kick_members=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("**Please specify a member**")
        return
    await member.ban()
    await ctx.send(f"{member.mention} Was banned by {ctx.author.mention}, [{reason}]")
# This displays an error if the user doesn't have the required permmissions
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("**Você não tem permissão para banir membros**")