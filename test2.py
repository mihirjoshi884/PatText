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
    docdir = "patents"
    # if not os.path.exists(docdir):
    #     os.mkdir(docdir)
    
    # path =os.path.join(os.chdir(document_loc),docdir)
    # absolute_path = os.path.join(path,f'{document_name}.text'.format(document_name))
    # print(absolute_path)
    # with open(absolute_path,"wb") as f:
    #     fnlist=[title,abstract,claims]
        
    #     for functions in fnlist :
    #         f.write(functions)

    print(os.getcwd())
    print(os.chdir('documents'))
    # print(os.chdir(document_loc))
    # print(os.getcwd())


    
get_url("https://patents.google.com/patent/US9416752?oq=ninad+joshi","gas turbine","Documents")

