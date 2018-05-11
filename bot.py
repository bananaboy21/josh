import discord
import os
from discord.ext import commands



bot = commands.Bot(command_prefix=">",owner_id=277981712989028353)


@bot.event
async def on_ready():
    print("Bot is online, and ready to ROLL!")


@bot.event
async def on_reaction_add(reaction, user):
    print(f"Used reaction: {reaction.emoji}")
    if reaction.emoji == "✅":
        x = discord.utils.get(bot.get_guild(417154444531204097).roles, name='Verified Member')
        await user.add_roles(x)
        
        
        
bot.run(os.environ.get("TOKEN"))
