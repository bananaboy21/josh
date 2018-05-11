import discord
import os
from discord.ext import commands



bot = commands.Bot(command_prefix=">",owner_id=277981712989028353)


@bot.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == "✅":
        x = discord.utils.get(user.guild.roles, name='Verified Member')
        await user.add_roles(x)
        
        
        
bot.run(os.environ.get("TOKEN"))
