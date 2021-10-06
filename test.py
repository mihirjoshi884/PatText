
import requests
from bs4 import BeautifulSoup

url = "https://patents.google.com/patent/US9416752?oq=ninad+joshi"

r = requests.get(url)
HtmlContent = r.content
soup = BeautifulSoup(HtmlContent , 'html.parser')

        
title = str(soup.title.text)
print(title)

        
abstract= str(soup.find("div",attrs={'class':'abstract'}).text)
print(abstract)

print("\n")
print("\n")
    
claim = soup.find_all("span",attrs={'itemprop':'count'})
no_claim = len(claim)
lenclaim =int(claim[no_claim - 1].text)
print(lenclaim)
    
    
# document_name = doc
# document_loc = loc
# docdir = "patents"
    
# path =os.path.join(os.getcwd(),docdir,document_loc)
# absolute_path = os.path.join(path,f'{document_name}.text'.format(document_name))
# print(absolute_path)
    
# if not os.path.exists(docdir):
#     os.mkdir(docdir)
    
# with open(absolute_path,"w") as f:
        
#     f.write("TILE -\r\n")
#     f.write(title)
#     f.write("\r\n")
#     f.write("Abstract -")
#     f.write("\r\n")
#     f.write(abstract)
#     f.write("\r\n")
#     f.write("Claims - ")
    
        # for i in range(1,lenclaim+1):
        #     if i <10:
        #         claim = soup.find('div',attrs={'id': f'CLM-0000{i}'.format(i)}).text
        #         f.write(str(claim))
        #     elif 10 <= i :
        #         claim = soup.find('div',attrs={'id': f'CLM-000{i}'.format(i)}).text
  
        #         f.write(str(claim))

# for i in range (0,lenclaim+1):
#     if i < 10:
#         claim= soup.find_all("div",attrs={'nums':f'0000{i}'.format(i)})
#         print(claim.text)
#     elif i >10 :
#         claim= soup.find_all("div",attrs={'nums':f'000{i}'.format(i)})
#         print(claim.text)

claims = soup.find_all("div",attrs={'class':'claim'})

for claim in claims :
    print(claim.text)
