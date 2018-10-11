import discord
import asyncio
import requests
import io
import commands as cmd
import config as cfg
import datetime
import pandas as pd
import json

client = discord.Client()
delay = 60

@client.event
async def on_ready():
    print('Bot loaded:')
    print(client.user.name, client.user.id)

@client.event
async def on_message(message):
    result_msg = ''
    try:
        if message.content.startswith(cfg.sign+'film') and message.author.top_role.name != cfg.admin_role:
            result_msg = '<@!%s>' % (message.author.id) + ' :no_entry: nope'
        elif message.content.startswith(cfg.sign+'film_get'):
            result_msg = cmd.rnd_film()
        elif message.content.startswith(cfg.sign+'films_last'):
            result_msg = cmd.last_films(message.content)
        elif message.content.startswith(cfg.sign+'film_add'):
            result_msg = cmd.add_film(message)
        elif message.content.startswith(cfg.sign+'film_watched'):
            result_msg = cmd.set_watched(message)
        elif message.content.startswith(cfg.sign+'dev'):
            result_msg = cmd.get_stats()
    except Exception as e:
        result_msg = '```'+'Exception: '+ str(e)+'```'
    await client.send_message(message.channel, result_msg)

client.run(cfg.token)