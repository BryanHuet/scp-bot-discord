import os
import io
import aiohttp
import discord
from discord.ext import commands
import logging
from datetime import datetime

from dotenv import load_dotenv
from operators import search_query, search_scp
from config import DATABASE, PAGE_LIST


logs = f'bot/logs/{datetime.now().strftime("%Y-%m-%d")}.log'

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(filename=logs, encoding='utf-8', mode='w'),
        logging.StreamHandler()
    ]
)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='|', intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'scp' in message.content.lower():
        logging.info('Find message with ' +
            f'scp mentionned: "{message.content.lower()}" ' +
            f'from author: "{message.author}" ' +
            f'from server: "{message.guild}'
        )
        
        q = search_query(message.content.lower())
        logging.info(
            f'Find scp-query: "{q}"')
        
        my_scp = search_scp(q, database=DATABASE, page_list=PAGE_LIST)
        logging.info(
            f'SCP found: {my_scp}')
        
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

if __name__ == '__main__':
    bot.run(TOKEN)
