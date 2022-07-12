import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!") > CMD PREFIX


@bot.event
async def on_ready():
    activity = discord.Activity(name="STATUS NAME", type=3)
    await bot.change_presence(status=discord.ActivityType.listening,
                              activity=activity)
    print("GO GO!")


@bot.command()
async def cmd0(ctx):
    embed = discord.Embed(
        title="TITLE",
        url="URL",
        description="DESCRIPTION",
        color=discord.Color.blue())
    await ctx.send(embed=embed)


@bot.command()
async def cmd1(ctx):
    await ctx.send("text")


@bot.command()
async def cmd2(ctx):
    await ctx.send("text")

@bot.command()
async def cmd3(ctx):
  await ctx.send("text")
  
@bot.command()
async def cmd4(ctx):
    embed = discord.Embed(title="TITLE",
                          url="URL",
                          description="DESCRIPTION",
                          color=discord.Color.blue())
    await ctx.send(embed=embed)


@bot.command()
async def cmd5(ctx):
    embed = discord.Embed(title="TITLE",
                          url="URL",
                          description="DESCRIPTION",
                          color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.command()
async def cmd6(ctx):
    embed = discord.Embed(title="TITLE",
                          url="",
                          description="DESCRIPTION",
                          color=discord.Color.blue())
    await ctx.send(embed=embed)


token = os.environ['TOKEN']
bot.run(token)
