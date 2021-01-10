"""CRUD film commands module"""
import random as rnd
import discord
from datetime import timedelta
import json
import config as cfg
from services import movie_search
from text_processing import wrap_code, wrap_text, combine_multiline

def load_json(filename: str):
    """
    Gets the json-file data
    """
    with open(filename, mode='w+', encoding='utf-8') as json_file:
        txt = json_file.read()
        return [] if not txt else json.loads(txt)

class Command:
    def __init__(self, keyword, method):
        self.keyword = keyword
        self.method = method

class FilmCommands:
    """
    Watch/watched film lists operations class
    """
    def __init__(self):
        self.watch_films = load_json("watch.json")
        self.watched_films = load_json("watched.json")

    def get_command(self, message, prefix):
        commands = [
            Command("films_all", self.get_all),
            Command("film_get", self.rnd_film),
            Command("films_last", self.last_films),
            Command("film_add", self.add_film),
            Command("film_watched", self.set_watched)
        ]
        for cmd in commands:
            if message.content.startswith(prefix + cmd.keyword):
                return cmd.method
        return None


    def add_film(self, msg):
        """
        Adds the film to watch list
        """
        words = msg.content.split(' ')
        name = (' '.join(words[1:])).lower().strip()
        updated = [film for film in self.watch_films if film['name'].lower() == name]

        if not updated:
            author, time = self.append_in_file(msg, name, 'watch')
            return ':white_check_mark: %s added by %s (%s)' % (name, author, time)
        return (':thinking: %s already added by %s (%s)' %
                (updated[0]['name'], updated[0]['sender'], updated[0]['time']))

    def append_in_file(self, msg, name, fl_name):
        """
        Appends new data in watch/watched files by pattern 'film name, message sender, message time'
        """
        with open(fl_name+'.json', mode='w', encoding='utf-8') as appendable_file:
            local_date = msg.created_at + timedelta(hours=cfg.gmt)
            date = local_date.strftime(cfg.datetime_format)
            author = msg.author.name
            new_item = {'name':name, 'sender':author, 'time':str(date)}
            if fl_name == 'watch':
                self.watch_films.append(new_item)
            else:
                self.watched_films.append(new_item)
            json.dump(self.watch_films, appendable_file, ensure_ascii=False)
        return author, date

    def last_films(self, message):
        """
        Gets the last n-watched films
        """
        if not self.watched_films:
            return ':sweat_smile: watched films list is empty'
        parts = message.content.split(' ')
        num = parts[len(parts) - 1]
        if num.isdigit():
            quantity = int(num)
            films = [film['name'] for film in self.watched_films[-1*quantity:]]
            return '\n'.join(films)
        return wrap_code('\nExample: !lastfilms 5\n')

    def rnd_film(self, msg):
        """
        Gets the random film in watch list
        """
        search = movie_search.MovieSearch(cfg.google_key, cfg.google_search_id)
        if not self.watch_films:
            return ':sweat_smile: empty films list'
        num = rnd.randint(0, len(self.watch_films) - 1)
        film = self.watch_films[num]
        header = f"Today's film: {film['name']} (Added by: {film['sender']})"
        body = "Link: " + search.get_movie_link(film['name'])
        return combine_multiline([wrap_text(header, ":film_frames:"), body])

    def set_watched(self, msg):
        """
        Moves film from watch list to watched
        """
        words = msg.content.split(' ')
        name = (' '.join(words[1:])).lower().strip()
        updated = [film for film in self.watch_films if film['name'].lower() != name]
        if len(watch_films) != len(updated):
            with open('watch.json', mode='w', encoding='utf-8') as wacth_file:
                json.dump(updated, wacth_file, ensure_ascii=False)
            self.append_in_file(msg, name, 'watched')
            watch_films = updated
            return ':thumbsup: Updated'
        return ':sweat_smile: Not found'

    def get_all(self, msg):
        """
        Displays all stored films
        """
        header = f":film_frames: Movies list :film_frames:"
        formatted_films = [':arrow_right: {0} (by {1} at {2})'.format(film["name"], film["sender"], film["time"]) 
            for film in self.watch_films]
        formatted_films.insert(0, header)
        return combine_multiline(formatted_films)
