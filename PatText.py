
from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import os
from tkinter import messagebox



def main ():

    root = Tk()
    root.geometry("2000x2000")
    root.title("PatText")
    document_no_list= []
    doc_list= []
    document_no= StringVar()
    DocNameVar= StringVar()
    
    Headinglabel= Label(root,text="PatText",font=("bold",70))
    Headinglabel.place(x=600,y=40)

    DocNumber = Label(root,text="Document number",font=("bold",22))
    DocNumber.place(x=400,y=300)
    Docname = Label(root,text="Document Name",font=("bold",22))
    Docname.place(x=400,y=350)
    
    DocLoc = Label(root,text= "Document LOCATION",font=("bold",22))
    DocLoc.place(x=400,y=400)

    DocNumberEntry = Entry(root,textvar= document_no)
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

    def add_btn_fn():
        document_no_list.append(document_no.get())
        doc_list.append(DocNameVar.get())
        DocNumberEntry.delete(0,END)
        DocNameEntry.delete(0,END)
        messagebox.showinfo("Information","Document information has been stored for the further process")


    add_btn = Button(text="ADD MORE DOCUMENTS",command= add_btn_fn)
    add_btn.place(x=750, y=450)

    


    
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
                    claim = soup.find('div',attrs={'id': f'CLM-0000{i}'.format(i)}).text
                    f.write(str(claim))
                elif 10 <= i :
                    claim = soup.find('div',attrs={'id': f'CLM-000{i}'.format(i)}).text
    
                    f.write(str(claim))
        
        def image_downloader(document_name):
            imgs = soup.find_all("img")
            print(len(imgs))
        
            names= []
            for i in range(1,len(imgs)+1):
                names.append(f'{document_name}{i}'.format(document_name,i)+'.jpg')

            link = []
            i = 0
            for img in imgs :
                link.append(img['src'])
            print(names,"\n")
            print(link,"\n")

            # path =os.path.join(os.getcwd(),docdir)
            # absolute_path = os.path.join(path,f'{document_name}.text'.format(document_name))
            # print(absolute_path)
    

            path =os.path.join(os.getcwd(),docdir)
            absolute_path = os.path.join(path,f'{document_name}images'.format(document_name))
            img_path = os.path.join(absolute_path,f'{names[i]}'.format(names[i]))

            if not os.path.exists(f'{document_name}images'.format(document_name)):
                os.mkdir(f'{document_name}images'.format(document_name))

            for i in range(0,len(link)):
                with open(absolute_path,'wb') as f:
                    im = requests.get(link[i])
                    f.write(im.content)
        
        image_downloader(document_name)

            
        
        messagebox.showinfo("ATTENTION ","your file/files has been processed")

    def DocProcessFn():
        DocNum = ""
        DocName = "" 
        
        if len(document_no_list) == len(doc_list) ==0 :

            DocNum = document_no.get()
            DocName = DocNameVar.get()
            scrapper(DocNum,DocName)
        elif len(document_no_list) == len (doc_list):
            
            for i in range(0,len(doc_list)):
                
                scrapper(document_no_list[i],doc_list[i])

        
        else :
            messagebox.showerror("Error", "insufficient data document information has been entered")
            quit()
            
        

    docprocess = Button(text="DocProcess",command= DocProcessFn)
    docprocess.place(x=600,y=450)
  
    root.mainloop()

if __name__ == "__main__":
    main()