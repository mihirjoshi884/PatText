
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

        
        r = requests.get(url)
        HtmlContent = r.content
        soup = BeautifulSoup(HtmlContent , 'html.parser')

        
        title = soup.title.text 
        print(title)

        
        abstract= soup.find("div",attrs={'id':'p-0001'})
        print(abstract.text)
        print("\n")
        print("\n")

        for i in range(1,13):
            
            if i <10:
                claims = soup.find('div',attrs={'id': f'CLM-0000{i}'.format(i)})
                print(claims.text)
            elif 10 <= i :
                claims = soup.find('div',attrs={'id': f'CLM-000{i}'.format(i)})
                print(claims.text) 


       
        if not os.path.exists(doc):
           os.mkdir(doc)

        filepath =os.path.join(os.path.realpath(os.getcwd()),doc) 
        with open(filepath,"wb") as f:
            fnlist=[title,abstract,claims]

            for functions in fnlist :
                f.write(functions)
        
    docprocess = Button(text="DocProcess",command= DocProcessFn)
    docprocess.place(x=600,y=450)
  
    





    root.mainloop()

if __name__ == "__main__":
    main()