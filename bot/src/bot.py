import os
import io
import httpx
import discord
from discord.ext import commands
import logging
from setproctitle import setproctitle

from dotenv import load_dotenv
from operators import search_query, search_scp
from config import DATABASE, PAGE_LIST

setproctitle("ScpBot")

logs = os.getenv('LOG_PATH', '/var/log/bots') + "/scp-bot-discord.log"

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
        message_source = message.content.lower()
        message_author = message.author.global_name
        message_server = message.guild.name

        log = {
            'source': message_source,
            'author': message_author,
            'server': message_server
        }

        query_found = search_query(message_source)
        log['query'] = query_found

        my_scp = search_scp(
            query_found, database=DATABASE, page_list=PAGE_LIST)
        log['scp'] = my_scp

        logging.info(log)

        if my_scp['name'] == 'NO SCP FOUND':
            return
        if my_scp['img'] == '':
            await message.channel.send(my_scp['name'])
        else:
            # get and send img
            try:
                async with httpx.AsyncClient() as session:
                    resp = await session.get(my_scp['img'])
                    if not resp:
                        return await message.channel.send(
                            'Could not download file...')
                    data = io.BytesIO(resp.content)
                    await message.channel.send(
                        my_scp['name'], file=discord.File(
                            data, my_scp['img'])
                    )
            except Exception as e:
                await message.channel.send(
                    my_scp['name'] + '\nLa photographie du ' +
                    'spécimen est en attente de déclassification.')
                raise e

if __name__ == '__main__':
    bot.run(TOKEN)
