"""Google search module"""
import json
import requests

class GoogleSearch:
    """Google search operations class"""
    def __init__(self, api_key, search_id):
        self.__api_key = api_key
        self.__search_id = search_id

    def search(self, query):
        """Gets the reponse of google search query"""
        if query == '':
            raise ValueError("Empty query!")
        response = (requests.get("https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=%s" %
                                 (self.__api_key, self.__search_id, query)))
        if response.status_code == 200:
            return response.content
        raise ValueError("Request error: {0}".format(response.status_code))

    def get_first_picture(self, query):
        """Gets the first picture by query"""
        response = json.loads(self.search(query))
        print(response['items'][0]['pagemap']['movie'][0])
        for temp in response['items']:
            print(temp['formattedUrl'])
        