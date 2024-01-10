import discord
from discord.ext import   commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(" >> Bot is online <<")


@bot.event
async def on_member_join(member):
    print(f'[member] join!')
    channel=bot.get_channel(1000325211603881995)
    await channel.send(f'[member]  join!')

@bot.event
async def on_member_remove(member):
    print(f'[member] leave!')
    channel = bot.get_channel(1000325281669709905)
    await channel.send(f'[member]  leave!')


bot.run('MTE5NDY0NTYxNTkwOTUzNTgxNQ.G45aFE.4Wrhj6Z6iElMPGreFiLP3T_z_3AKD7Y_mbeD1k')
