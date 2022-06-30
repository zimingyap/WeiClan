import discord
import random
import config

TOKEN = config.TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print("We have log in as {0.user}".format(client))
    
client.run(TOKEN)