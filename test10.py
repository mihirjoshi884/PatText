from tkinter import *
from tkinter import ttk
from scraper import *

def main ():

    root = Tk()
    root.geometry("2000x2000")
    root.title("PatText")
    
    url_var= StringVar()
    DocNameVar= StringVar()
    
    Headinglabel= Label(root,text="PatText",font=("bold",70))
    Headinglabel.place(x=600,y=40)

    DocNumber = Label(root,text="Document number",font=("bold",22))
    DocNumber.place(x=400,y=300)
    Docname = Label(root,text="Document Name",font=("bold",22))
    Docname.place(x=400,y=350)
    
    DocLoc = Label(root,text= "Document LOCATION",font=("bold",22))
    DocLoc.place(x=400,y=400)

    DocNumberEntry = Entry(root,textvar= url_var)
    DocNumberEntry.place(x=700 ,y = 300)

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
        
        url =str(url_var.get())
        doc = str(DocNameVar.get())
        loc = str(dropdown.get())

        scrape = scrapper(url,doc,loc)
            
        

    docprocess = Button(text="DocProcess",command= DocProcessFn)
    docprocess.place(x=600,y=450)
  
    root.mainloop()



main()