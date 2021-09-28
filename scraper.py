import requests
from bs4 import BeautifulSoup
import os


class scrapper :

    def __init__(self,url,doc,loc):
        
        self.url = url
        self.doc = doc
        self.loc = loc

    def get_url(self):
        
        self.url
        print(self.url)
        return self.url 

    def get_doc(self):
        self.doc 
        print(self.doc)
        return self.doc

    def get_loc(self):
        self.loc
        print(self.loc)
        return self.loc


