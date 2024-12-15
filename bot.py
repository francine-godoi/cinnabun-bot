from discord import Intents
from discord.ext import commands

import os
import asyncio
from dotenv import load_dotenv

# setup bot
bot = commands.Bot(command_prefix="!", intents=Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Get token from file .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Load cogs
async def load():
    for filename in os.listdir("./cogs"):        
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")            

# Call function to load cogs and run the bot
async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)

asyncio.run(main())