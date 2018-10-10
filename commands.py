import io
import random as rnd
from time import sleep
from datetime import date
import requests
import json
import config as cfg

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
    parts = req.split(' ')
    num = parts[len(parts)-1]
    if num.isdigit():
        quantity = int(num)
        films = watched_films[-1*quantity:]
        return ''.join(films)
    else:
        return '```\nExample: !lastfilms 5\n```'

def rnd_film():
    num = rnd.randint(0,len(watched_films)-1)
    msg = ":video_camera: Today's film: " + watch_films[num]
    return msg

def get_stats():
    response = requests.get(cfg.repo_url)
    info = json.loads(response.text)
    total_commits = len(info)    
    commit_info = info[0]['commit']['author']
    date = commit_info['date']
    name = commit_info['name']
    return 'Total commits: %s. Last commit by %s (%s)' % (total_commits, name, date)
