import io
import random as rnd
from time import sleep
from datetime import date

with open('watch.txt', encoding='utf-8') as fl:
    watch_films = fl.readlines()
with open('watched.txt', encoding='utf-8') as fl:
    watched_films = fl.readlines()

def add_film(req):
    words = req.split(' ')
    name = ' '.join(words[1:])
    with open('watch.txt', mode='a', encoding='utf-8') as fl:
        fl.write('\n'+name)
    return name + ' added'

def last_films(req):
    num = get_second_part(req)
    if num.isdigit():
        quantity = int(num)
        films = watched_films[-1*quantity:]
        return ''.join(films)
    else:
        return '```\nExample: !lastfilms 5\n```'

def get_second_part(msg):
    parts = msg.split(' ')
    last = parts[len(parts)-1]
    return last

def rnd_film():
    num = rnd.randint(0,len(watched_films)-1)
    msg = ':video_camera: Сегодня фильм: '+watch_films[num]
    return msg
