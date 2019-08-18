import extensions.google_search as google_search
import config
import json

class MovieSearch:
    def __init__(self, google_key, google_search_id):
        self.search_module = google_search.GoogleSearch(google_key,google_search_id)

    def get_movie_link(self, movie_name):        
        response = json.loads(self.search_module.search(movie_name))
        return response['items'][0]['formattedUrl']

    def get_movie_image_link(self, movie_name):
        response = json.loads(self.search_module.search(movie_name))
        return response['items'][0]['pagemap']['cse_image'][0]['src']