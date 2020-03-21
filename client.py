# bot.py
import os
import discord
from dotenv import load_dotenv
from hooker import find_stats

load_dotenv()
TOKEN = os.getenv('API_TOKEN')
GUILD = os.getenv('SERVER_NAME')
client = discord.Client()


@client.event
# async def on_ready():

async def on_message(message):
    guild = discord.utils.find(lambda g: g.name == GUILD,\
    client.guilds)
    if message.author == client.user:
        return

    command = message.content.split()

    if command[0] != '!corona':
        return

    if len(command) > 1:
        country = command[1]
        total, dead, recovered = find_stats(country)
    else:
        total, dead, recovered = find_stats()


    
    await message.channel.send(f"Current Corona Virus Stats:\n{total} total people infected \n{dead} total dead \n{recovered} total recovered")

    print(f'{client.user} has connected to Discord!')
    print(f'{guild.name}(id: {guild.id}')

client.run(TOKEN)