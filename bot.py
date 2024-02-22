import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

@bot.command()
async def addrole(ctx,role: discord.role, user: discord.member):
    if ctx.author.guild_permissions.administrator:
        await user.add_role(role)
        await ctx.send(f"Роль выдана! {role.mention} to {user.mention}.")

@bot.command()
async def removerole(ctx, role: discord.role, user: discord.member):
    if ctx.author.guild_permissions.administrator:
        await user.remove_role(role)
        await ctx.send(f"Роль убрана! {role.mention} to {user.mention}.")

bot.run("")
