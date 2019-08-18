import discord
import asyncio
import requests
import io
import commands as cmd
import config as cfg
import json

client = discord.Client()
delay = 60

@client.event
async def on_ready():
    print('Bot loaded:')
    print(client.user.name, client.user.id)

@client.event
async def on_message(message):
    channel = client.get_channel(message.channel.id)
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
        else:
            result_msg = ":x: Unknown command"
    except Exception as e:
        code_quote = '`' * 3
        result_msg = code_quote +'An exception occured: '+ str(e) + code_quote
    if result_msg:
        await channel.send(result_msg)

if cfg.token:
    client.run(cfg.token)
else:
    raise Exception("There is no token in config file")