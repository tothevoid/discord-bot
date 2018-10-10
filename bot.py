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
    if message.content.startswith(cfg.sign+'film'):
        await client.send_message(message.channel, cmd.rnd_film())
    elif message.content.startswith(cfg.sign+'lastfilms'):
        await client.send_message(message.channel, cmd.last_films(message.content))
    elif message.content.startswith(cfg.sign+'addfilm'):
        await client.send_message(message.channel, cmd.add_film(message.content))
    elif message.content.startswith(cfg.sign+'dev'):
        await client.send_message(message.channel, cmd.get_stats())

client.run(cfg.token)