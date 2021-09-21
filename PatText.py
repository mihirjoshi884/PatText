
from tkinter import *
from tkinter import ttk 

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
        url = urlvar.get()
        doc = DocNameVar.get()
        loc = dropdown.get()


        print(url)
        print(doc)
        print(loc)
        
    docprocess = Button(text="DocProcess",command= DocProcessFn)
    docprocess.place(x=600,y=450)
  
    





    root.mainloop()

if __name__ == "__main__":
    main()