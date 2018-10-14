import requests
import json 

class GoogleSearch:
    def __init__(self, APIKey, search_id):
        self.__APIKey = APIKey
        self.__search_id = search_id

    def search(self, query):
        if query == '':
            raise ValueError("Empty query!")
        response = requests.get("https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=%s" % (self.__APIKey,self.__search_id,query))        
        if response.status_code == 200:
            return response.content
        else:
            raise ValueError("Request error: {0}".format(response.status_code))

    def get_first_picture(self, query):
        response = json.loads(self.search(query))
        print(response['items'][0]['pagemap']['movie'][0])
        for temp in response['items']:
            print(temp['formattedUrl'])
        
        


#search = GoogleSearch("AIzaSyCHMkHMPdFwvGAQJ0BaftqDOs1tC5uO8m8", "011702783576759763128:jceivjlr5q0")
#print(search.search("matrix"))
#print(search.get_first_picture("matrix"))