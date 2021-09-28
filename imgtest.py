import requests
import os
from bs4 import BeautifulSoup

url = "https://patents.google.com/patent/US6612106?oq=ninad+joshi"
r = requests.get(url)

soup= BeautifulSoup(r.text,'html.parser')
document_name= " ninad joshi"

imgs = soup.find_all("img")
print(len(imgs))
names= []
for i in range(1,len(imgs)+1):
    names.append(f'{document_name}{i}'.format(document_name,i)+'.jpg')

link = []
for img in imgs :
    link.append(img['src'])
for i in range(0,len(link)):
    with open(names[i],'wb') as f:
        im = requests.get(link[i])
        f.write(im.content)


print(names,"\n")
print(link,"\n")