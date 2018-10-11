import io
import random as rnd
from time import sleep
from datetime import datetime, timedelta
import requests
import json
import config as cfg

with open('watch.json', mode='w+', encoding='utf-8') as fl:
    txt = fl.read()
    if txt == '':
        watch_films = []
    else:    
        watch_films = json.loads(txt)
with open('watched.json', mode='w+', encoding='utf-8') as fl:
    txt = fl.read()
    if txt == '':
        watched_films = []
    else:
        watched_films = json.loads(txt)

def add_film(msg):
    words = msg.content.split(' ')
    name = (' '.join(words[1:])).lower().strip()
    updated = [film for film in watch_films if film['name'].lower()==name]

    if (len(updated)==0):
        author, time = append_in_file(msg, name, 'watch')
        return ':white_check_mark: %s added by %s (%s)' % (name, author, time)
    else:
        return ':thinking: %s already added by %s (%s)' % (updated[0]['name'], updated[0]['sender'], updated[0]['time'])

def append_in_file(msg, name, fl_name):
    with open(fl_name+'.json', mode='w', encoding='utf-8') as fl:
        local_date = msg.timestamp + timedelta(hours=cfg.gmt)
        date = local_date.strftime(cfg.datetime_format)
        author = msg.author.name
        new_item = {'name':name,'sender':author,'time':str(date)}
        if (fl_name == 'watch'):
            watch_films.append(new_item)
        else:
            watched_films.append(new_item)
        json.dump(watch_films, fl, ensure_ascii=False)
    return author, date

def last_films(req):
    if (len(watched_films)==0):
        return ':sweat_smile: empty watched films list'
    parts = req.split(' ')
    num = parts[len(parts)-1]
    if num.isdigit():
        quantity = int(num)
        films = [film['name'] for film in watched_films[-1*quantity:]]
        return '\n'.join(films)
    else:
        return '```\nExample: !lastfilms 5\n```'

def rnd_film():
    if (len(watch_films)==0):
        return ':sweat_smile: empty films list'
    num = rnd.randint(0,len(watch_films)-1)
    msg = ":video_camera: Today's film: " + watch_films[num]['name']
    return msg

def set_watched(msg):
    global watch_films
    words = msg.content.split(' ')
    name = (' '.join(words[1:])).lower().strip()
    updated = [film for film in watch_films if film['name'].lower()!=name]
    if (len(watch_films)!=len(updated)):
        with open('watch.json', mode='w', encoding='utf-8') as fl:
            json.dump(updated, fl, ensure_ascii=False)
        append_in_file(msg, name, 'watched')
        watch_films = updated
        return ':thumbsup: Updated'
    else:
        return ':sweat_smile: Not found'

def get_stats():
    response = requests.get(cfg.repo_url)
    info = json.loads(response.text)
    total_commits = len(info)    
    commit_info = info[0]['commit']['author']
    name = commit_info['name']
    local_date = datetime.strptime(commit_info['date'],'%Y-%m-%dT%H:%M:%SZ') + timedelta(cfg.gmt)
    date = local_date.strftime(cfg.datetime_format)
    return 'Total commits: %s. Last commit by %s (%s)' % (total_commits, name, date)