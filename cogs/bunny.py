import discord
from discord.ext import commands
from random import choice
import asyncpraw as praw
import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv('client_id')
CLIENT_SECRET = os.getenv('client_secret')
USER_AGENT = os.getenv('user_agent')

class Bunny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")

    @commands.command()
    async def bunny(self, ctx: commands.Context):

        subreddit = await self.reddit.subreddit("Bunnies")
        post_list = []

        async for post in subreddit.hot(limit=30):
            if not post.over_18 and any(post.url.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".gif"]):
                author_name = post.author.name or "N/A"
                post_list.append((post.url, author_name))

        if post_list:
            random_post = choice(post_list)

            bunny_embed = discord.Embed(title="🐇 Bunny! 🐇", color=discord.Color.random())
            bunny_embed.set_image(url=random_post[0])
            bunny_embed.set_footer(text=f"Post created by {random_post[1]}.")

            await ctx.send(embed=bunny_embed)

        else:
            await ctx.send("Couldn't find any'bunny', try again later.")

    def cog_unload(self):
        self.bot.loop.create_task(self.reddit.close())


async def setup(bot):
    await bot.add_cog(Bunny(bot))   