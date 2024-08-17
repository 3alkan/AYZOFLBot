import discord
import traceback
from discord import Game
import os
from dotenv import load_dotenv

# to learn library version
#print(discord.version_info)

load_dotenv()
token=os.getenv("AYZOFLBot_Token")

intents=discord.Intents.default()
client=discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    #await client.change_presence(activity=Game(name="Playing chess"))
    for guild in client.guilds:
        print(guild.name)

@client.event
async def on_error(event, *args, **kwargs):
    print(f"An error occurred in {event}:")
    traceback.print_exc()


client.run(token)