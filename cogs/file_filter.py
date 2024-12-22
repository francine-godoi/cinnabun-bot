from typing import List
import discord
from discord.ext import commands

class FileFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.accepted_extentions: List[str] = [".png", ".jpg", ".jpeg", ".gif"]        
        self.bots_and_staff_id: List[int] = [1317830592431394846, # CINNABUN_BOT_ID
                                             1125940432136847380] # MY_ADMIN_ID

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.id in self.bots_and_staff_id:
            return
        
        for file in message.attachments:
            if not any(file.filename.endswith(ext) for ext in self.accepted_extentions):
                await message.delete()

                bad_file_embed = discord.Embed(title=":rotating_light: Unsuppoted filetype! :rotating_light:", color=discord.Color.red())

                error_message = f"{message.author.mention}, your message contained an unsupported file of filetype: .{file.filename.split('.')[-1]}.\n\nThe supported filetypes are: {' | '.join(self.accepted_extentions)}"

                bad_file_embed.add_field(name="", value=error_message, inline=False)

                await message.channel.send(embed=bad_file_embed)


async def setup(bot):
    await bot.add_cog(FileFilter(bot))
