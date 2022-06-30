import discord
import random

TOKEN = 'OTkxOTk3NTEzNzEwMTg2NTQ2.G4x5Vs.88AjQX9Uoi0ZEq8Yll3qvp8KFgKFY6Dpz4vVvM'

client = discord.Client()

@client.event
async def on_ready():
    print("We have log in as {0.user}".format(client))
    
client.run(TOKEN)