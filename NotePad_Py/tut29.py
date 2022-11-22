from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename,asksaveasfilename    #this are libraries used for opening anad saving the file
import os

#function 
def newFile():
    global file
    root.title("Untitled Document")
    file = None
    text.delete(1.0,END)        #this will delete all the text from area

def openFile():
    global file
    file = askopenfilename()
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" -Notepad")
        text.delete(1.0,END)
        f = open(file,"r")
        text.insert(1.0,f.read())   #insertion will start from start to end of readable line
        f.close()
        
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
        if file == "#":
            file = None
        else:
            #save as a new file
            f = open(file,"w")
            f.write(text.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " -Notepad")
            print("File Save")
    else:
        #save the file
        f = open(file,"w")
        f.write(text.get(1.0,END))
        f.close()

def Cut():
    text.event_generate(("<<Cut>>"))  #event generator genrates any events
def Copy():
    text.event_generate(("<<Copy>>"))
def Paste():
    text.event_generate(("<<Paste>>"))
def HelpFunc():
    msg.showinfo("About","This is our new notepad. \nIt has multiple functions like copy paste")

#GUI
root = Tk()
root.geometry("600x600")
root.title("NotePad")
root.wm_iconbitmap("i.ico")

#adding text area
text = Text(root,font="lucidia 15")
text.pack(fill=BOTH,expand=True)

#creating a scrollbar
scrollbar = Scrollbar(text)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)

#creating a file to save the text
file = None

#creating a main menu bar
main_menu = Menu(root)

#File menu starts from here
FileMenu = Menu(main_menu,tearoff=0)

#to open new file
FileMenu.add_command(label="New File",command=newFile)

#to open already existing file
FileMenu.add_command(label="Open File",command=openFile)

#to save current file
FileMenu.add_command(label="Save",command=saveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit",command=quit)
main_menu.add_cascade(label="File",menu=FileMenu)
root.config(menu=main_menu)

#Edit menu
EditMenu = Menu(main_menu,tearoff=0)

#Cut feature
EditMenu.add_command(label="Cut",command=Cut)
EditMenu.add_command(label="Copy",command=Copy)
EditMenu.add_command(label="Paste",command=Paste)
main_menu.add_cascade(label="Edit",menu=EditMenu)

#Help menu
HelpMenu = Menu(main_menu,tearoff=0)
HelpMenu.add_command(label="Help",command=HelpFunc)
main_menu.add_cascade(label="Help",menu=HelpMenu)


root.mainloop()