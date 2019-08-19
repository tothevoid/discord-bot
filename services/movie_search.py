"""Movie search operations module"""
import json
from services.google_search import GoogleSearch

class MovieSearch:
    """Google movie search class"""
    def __init__(self, google_key, google_search_id):
        self.search_module = GoogleSearch(google_key, google_search_id)

    def get_movie_link(self, movie_name):
        """Gets the movie link by movie name"""
        response = json.loads(self.search_module.search(movie_name))
        return response['items'][0]['formattedUrl']

    def get_movie_image_link(self, movie_name):
        """Gets the movies image by movie name"""
        response = json.loads(self.search_module.search(movie_name))
        return response['items'][0]['pagemap']['cse_image'][0]['src']
