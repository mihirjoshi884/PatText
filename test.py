
import requests
from bs4 import BeautifulSoup

url = "https://patents.google.com/patent/US9416752?oq=ninad+joshi"

r = requests.get(url)
HtmlContent = r.content

soup = BeautifulSoup(HtmlContent , 'html.parser')

title = soup.title.text 
print(title)

descript = set()

# for name in meta :

#     descriptText = name.get()
#     descript.add(descriptText)
#     print(descript)

# for tag in soup.find_all("meta"):
#     if tag.get("property", None) == "og:description":
#         descript.add( tag.get("content", None) )
#         print(descript)

des = soup.find("meta",attrs={'name':'description'})
print(des["content"])