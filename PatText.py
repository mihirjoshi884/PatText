
from tkinter import *
from tkinter import ttk 
import requests
from bs4 import BeautifulSoup
import os



def main ():

    root = Tk()
    root.geometry("2000x2000")
    root.title("PatText")

    urlvar= StringVar()
    DocNameVar= StringVar()
    
    Headinglabel= Label(root,text="PatText",font=("bold",70))
    Headinglabel.place(x=600,y=40)

    URL = Label(root,text="URL",font=("bold",22))
    URL.place(x=400,y=300)
    Docname = Label(root,text="Document Name",font=("bold",22))
    Docname.place(x=400,y=350)
    
    DocLoc = Label(root,text= "Document LOCATION",font=("bold",22))
    DocLoc.place(x=400,y=400)

    UrlEntry = Entry(root,textvar= urlvar)
    UrlEntry.place(x=700 ,y = 300)

    DocNameEntry = Entry(root,textvar= DocNameVar)
    DocNameEntry.place(x=700 ,y = 350)


    lists = [
        "documents",
        "downloads",
        "desktop"    
    ]

    dropdown = ttk.Combobox(root,values= lists)
    dropdown.place(x=700,y=400)

    def DocProcessFn():
        url = str(urlvar.get())
        doc = str(DocNameVar.get())
        loc = str(dropdown.get())

        
        surl = url
        r = requests.get(url)
        HtmlContent = r.content
        soup = BeautifulSoup(HtmlContent , 'html.parser')

        
        title = str(soup.title.text)
        print(title)

        
        abstract= str(soup.find("div",attrs={'id':'p-0001'}).text)
        print(abstract)

        print("\n")
        print("\n")
    
        claim = soup.find_all("span",attrs={'itemprop':'count'})
        no_claim = len(claim)
        lenclaim =int(claim[no_claim - 1].text)
        print(lenclaim)
    
    
        document_name = doc
        document_loc = loc
        docdir = "patents"
    
        path =os.path.join(os.getcwd(),docdir,document_loc)
        absolute_path = os.path.join(path,f'{document_name}.text'.format(document_name))
        print(absolute_path)
    
        if not os.path.exists(docdir):
            os.mkdir(docdir)
    
        with open(absolute_path,"w") as f:
        
            f.write("TILE -\r\n")
            f.write(title)
            f.write("\r\n")
            f.write("Abstract -")
            f.write("\r\n")
            f.write(abstract)
            f.write("\r\n")
            f.write("Claims - ")
    
            for i in range(1,lenclaim+1):
                if i <10:
                    claim = soup.find('div',attrs={'id': f'CLM-0000{i}'.format(i)}).text
                    f.write(str(claim))
                elif 10 <= i :
                    claim = soup.find('div',attrs={'id': f'CLM-000{i}'.format(i)}).text
  
                    f.write(str(claim))          
        
        
    docprocess = Button(text="DocProcess",command= DocProcessFn)
    docprocess.place(x=600,y=450)
  
    root.mainloop()

if __name__ == "__main__":
    main()