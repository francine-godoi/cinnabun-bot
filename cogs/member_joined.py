import discord
from discord.ext import commands
import random

class MemberJoined(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        welcome_channel = member.guild.system_channel
        
        with open("quotes/welcome_quotes.txt", "r", encoding='utf-8') as file:
            welcome_msg = file.readlines()

        randomized_msg = random.choice(welcome_msg)
        await welcome_channel.send(f"Welcome! {randomized_msg}")         


async def setup(bot):
    await bot.add_cog(MemberJoined(bot))