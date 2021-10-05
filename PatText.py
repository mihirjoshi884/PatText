
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import requests
from bs4 import BeautifulSoup
import os
from tkinter import messagebox
import csv



def main ():

    root = Tk()
    root.geometry("2000x2000")
    root.title("PatText")
    document_no_list= []
    doc_list= []
    document_no= StringVar()
    DocNameVar= StringVar()
    filepath= StringVar()


    Headinglabel= Label(root,text="PatText",font=("bold",70))
    Headinglabel.place(x=600,y=40)

    DocNumber = Label(root,text="US-PATENT NUMBER",font=("bold",22))
    DocNumber.place(x=200,y=300)
    Docname = Label(root,text="FILE-Name",font=("bold",22))
    Docname.place(x=200,y=350)
    
    DocLoc = Label(root,text= "Document-LOCATION",font=("bold",22))
    DocLoc.place(x=200,y=400)

    FILE_PATH= Label(root,text="FILE-PATH",font=("bold",22))
    FILE_PATH.place(x=750,y=300)

    filepathentry = Entry(root,textvar= filepath,width=50)
    filepathentry.place(x=900,y=300)

    DocNumberEntry = Entry(root,textvar= document_no)
    DocNumberEntry.place(x=450 ,y = 300)

    DocNameEntry = Entry(root,textvar= DocNameVar)
    DocNameEntry.place(x=450 ,y = 350)

    def scrapper(doc_no,doc_name):
        url=f'https://patents.google.com/patent/{doc_no}'.format(doc_no)
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
    
    
        document_name = doc_name
        
        print(document_name)
        
        # document_loc = loc
        docdir = "patents"

        path =os.path.join(os.getcwd(),docdir)
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
                    claim = soup.find('div',attrs={'class':'claim-text'}).text
                    f.write(str(claim))
                elif 10 <= i :
                    claim = soup.find('div',attrs={'class':'claim-text'}).text
        
                    f.write(str(claim))
                

        
        def image_downloader(document_name):
            imgs = soup.find_all("img")
            print(len(imgs))
        
            names= []
            for i in range(1,len(imgs)+1):
                names.append(f'{document_name}{i}'.format(document_name,i)+'.jpg')

            link = []
            
            
            # path =os.path.join(os.getcwd(),docdir)
            # absolute_path = os.path.join(path,f'{document_name}.text'.format(document_name))
            # print(absolute_path)
    

            path =os.path.join(os.getcwd(),docdir)
            absolute_path = os.path.join(path,f'{document_name}images'.format(document_name))
            print(absolute_path)
            if not os.path.exists(absolute_path):
                os.mkdir(absolute_path)
            for img in imgs :
                link.append(img['src'])
            print(names,"\n")
            print(link,"\n")

            

            

            for i in range(0,len(link)):
                img_path = os.path.join(absolute_path,f'{names[i]}'.format(names[i]))
                print(img_path)
            
                with open(img_path,'wb') as f:
                    im = requests.get(link[i])
                    f.write(im.content)
        
        image_downloader(document_name)

            
        
        

    def DocProcessFn():
        DocNum = ""
        DocName = "" 
        
        if len(document_no_list) == len(doc_list) ==0 :

            DocNum = document_no.get()
            DocName = DocNameVar.get()
            scrapper(DocNum,DocName)
            messagebox.showinfo("ATTENTION ","your file/files has been processed")
        elif len(document_no_list) == len (doc_list):
            
            for i in range(0,len(doc_list)):
                
                scrapper(document_no_list[i],doc_list[i])
            messagebox.showinfo("ATTENTION ","your file/files has been processed")
        
        else :
            messagebox.showerror("Error", "insufficient data document information has been entered")
            quit()

    def getfile():
        file = filepath.get()
        import pandas as pd
        csv= pd.read_csv(file,usecols=['PATENT-NUMBER','PATENT-NAME'])
        df= pd.DataFrame(csv)


        document_no_list=df['PATENT-NUMBER'].dropna().tolist()

        print(document_no_list)
        doc_list=df['PATENT-NAME'].dropna().tolist()
        print(doc_list)

        print(len(document_no_list))
        print(len(doc_list))

        for i in range (0,len(doc_list)):
            scrapper(document_no_list[i],doc_list[i])

    
    file_path_btn = Button(root,text="Process File",command= getfile)
    file_path_btn.place(x=1100,y=350) 

    lists = [
        "documents",
        "downloads",
        "desktop"    
    ]

    dropdown = ttk.Combobox(root,values= lists)
    dropdown.place(x=450,y=400)

    def add_btn_fn():
        document_no_list.append(document_no.get())
        doc_list.append(DocNameVar.get())
        DocNumberEntry.delete(0,END)
        DocNameEntry.delete(0,END)
        messagebox.showinfo("Information","Document information has been stored for the further process")


    add_btn = Button(text="ADD MORE DOCUMENTS",command= add_btn_fn)
    add_btn.place(x=450, y=500)

    


    
    
            
        

    docprocess = Button(text="DocProcess",command= DocProcessFn)
    docprocess.place(x=250,y=500)

  
    root.mainloop()

if __name__ == "__main__":
    main()