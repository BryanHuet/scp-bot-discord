import os
import io
import aiohttp
import discord

from dotenv import load_dotenv
from operators import search_query, search_scp

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'scp' in message.content.lower():
        q = search_query(message.content.lower())

        my_scp = search_scp(q)

        if my_scp['img'] == '':
            await message.channel.send(my_scp['name'])
        else:
            # get and send img
            async with aiohttp.ClientSession() as session:
                async with session.get(my_scp['img']) as resp:
                    if resp.status != 200:
                        return await message.channel.send(
                            'Could not download file...')
                    data = io.BytesIO(await resp.read())
                    await message.channel.send(
                        my_scp['name'], file=discord.File(data, my_scp['img']))

client.run(TOKEN)
