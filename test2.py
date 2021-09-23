import requests
from bs4 import BeautifulSoup
from requests.models import super_len
import os


def get_url(url,doc,loc):
    global surl
    surl = url
    r = requests.get(url)
    HtmlContent = r.content
    soup = BeautifulSoup(HtmlContent , 'html.parser')

    global title
    title = soup.title.text 
    print(title)

    global abstract
    abstract= soup.find("div",attrs={'id':'p-0001'})
    print(abstract.text)
    print("\n")
    print("\n")

    for i in range(1,13):
        global claims
        if i <10:
            claims = soup.find('div',attrs={'id': f'CLM-0000{i}'.format(i)})
            print(claims.text)
        elif 10 <= i :
            claims = soup.find('div',attrs={'id': f'CLM-000{i}'.format(i)})
            print(claims.text) 


    document_name = doc
    document_loc = loc
    if not os.path.exists(document_name):
        os.mkdir(document_name)
    
    filepath =os.path.join(os.path.realpath(os.getcwd()),document_name) 
    with open(filepath,"wb") as f:
        fnlist=[title,abstract,claims]
        
        for functions in fnlist :
            f.write(functions)

    


