
import requests
from bs4 import BeautifulSoup

url = "https://patents.google.com/patent/US9416752?oq=ninad+joshi"

r = requests.get(url)
HtmlContent = r.content

soup = BeautifulSoup(HtmlContent , 'html.parser')

title = soup.title.text 
print(title)




des = soup.find("meta",attrs={'name':'description'})
print(des["content"])

abstract= soup.find("div",attrs={'id':'p-0001'})
print(abstract.text)
print("\n")
print("\n")

# for i in range(1,13):
#     if i <10:
#         claim = soup.find('div',attrs={'id': f'CLM-0000{i}'.format(i)})
#         print(claim.text)
#     elif 10 <= i :
#         claim = soup.find('div',attrs={'id': f'CLM-000{i}'.format(i)})
  
#         print(claim.text) 


claim = soup.find_all("span",attrs={'itemprop':'count'})
print(claim)

imgs = soup.find_all("img")

for img in imgs :

    print(img['src'])