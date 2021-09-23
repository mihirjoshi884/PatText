import requests
from bs4 import BeautifulSoup

class scrapper :

    def __init__(self,url,doc,loc):
        
        self.url = url
        self.doc = doc
        self.loc = loc

    def get_url(self):

        return self.url 

    def get_doc(self):

        return self.doc

    def get_loc(self):
        return self.loc

scrapper.get_url(f"https://www.google.com")   