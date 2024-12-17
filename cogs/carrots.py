import discord
from discord.ext import commands
import random

class Carrots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")

    @commands.command()
    async def carrot(self, ctx: commands.Context):

        with open("quotes/quotes.txt", "r", encoding='utf-8') as file:
            message = file.readlines()

        randomized_msg = random.choice(message)

        embed = discord.Embed(title="🥕 Carrot!! 🥕", colour = discord.Colour.random())
        embed.add_field(name="", value=(f"{randomized_msg}"), inline=False)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Carrots(bot))        