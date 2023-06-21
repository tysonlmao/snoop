import discord
import os

from server import get_hypixel_data

# set client intents
intents = discord.Intents.default()
intents.message_content = True

# environmental variables
bot_token = "???"

# create a client
client = discord.Client(intents=intents)
prefix = "snoop "

# on_ready
# log connection
@client.event 
async def on_ready():
    await client.change_presence(activity=discord.Game(name="0.0.1"))
    print(f'{client.user} connected to station.')

@client.event
async def on_message(message):
    if message.author == client.user: 
        return
    
    if message.content.startswith(prefix + "test"):
        x = get_hypixel_data('f138952a-3492-4573-80db-d928fd3cde33')
        y = x['player']['displayname']
        await message.channel.send(y)


# client command
@client.command()
async def stats(ctx, uuid): 
    x = get_hypixel_data(uuid)
    y = x['player']['displayname']
    await ctx.send

# run the client
client.run(bot_token)