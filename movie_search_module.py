import google_search_module.search_module as google_module
import config
import json

class MovieSearch:
    def __init__(self, google_key, google_search_id):
        self.search_module = google_module.GoogleSearch(google_key,google_search_id)

    def get_kinopoisk_link(self, movie_name):        
        response = json.loads(self.search_module.search(movie_name))
        return response['items'][0]['formattedUrl']

    def get_movie_image_link(self, movie_name):
        response = json.loads(self.search_module.search(movie_name))
        return response['items'][0]['pagemap']['movie'][0]['image']
