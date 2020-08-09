'''
DEEPANSHU RAWAT
'''
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from fpdf import FPDF 
import os

root = Tk()


#CREATING A NEW FILE
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

#OPENING A FILE
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


#SAVING A FILE 
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

#SIMPLE COMMANDS FOR FREQUENT USE
def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<Cut>"))

def copy():
    TextArea.event_generate(("<Copy>"))

def paste():
    TextArea.event_generate(("<Paste>"))

def about():
    showinfo("Notepad", "Notepad by Code With DEEPANSHU RAWAT")

#FINDING A GIVEN WORD
def find(): 
      
    text.tag_remove('found', '1.0', END)  
    s = edit.get()  
    if s: 
        idx = '1.0'
        while 1: 
            idx = text.search(s, idx, nocase=1,  
                              stopindex=END)  
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))  
            text.tag_add('found', idx, lastidx)  
            idx = lastidx 
        text.tag_config('found', foreground='red')  
    edit.focus_set() 


#PDF GENERATION
inputValue=""
def pdf_converter():
    def retrieve_input():
        inputValue = TextArea.get("1.0",END)

    pdf = FPDF()
    pdf.add_page() 
    pdf.set_font("Arial", size = 15) 
    pdf.cell(200, 10, txt = inputValue, align = 'C') 
    pdf.cell(200, 10, txt = inputValue ,  align = 'C') 
    pdf.output("your_text.pdf")


if __name__ == '__main__':
    
    
    root.title("Untitled - Notepad")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font=("Courier", 20, "italic", "bold"))
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    #FINDING METHOD
    fram = Frame(root) 
    Label(fram,text='Text to find:').pack(side=LEFT)  
    edit = Entry(fram)  
    edit.pack(side=LEFT, fill=Y, expand=1)  
    edit.focus_set()  
    butt = Button(fram, text='Find')   
    butt.pack(side=RIGHT)  
    fram.pack(side=TOP) 
  
  
    text = TextArea 
    butt.config(command=find) 


    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile, font=("Arial", 14))

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile, font=("Arial", 14))

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile, font=("Arial", 14))
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp, font=("Arial", 14))
    MenuBar.add_cascade(label = "File", menu=FileMenu, font=("Arial", 20))
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut, font=("Arial", 14))
    EditMenu.add_command(label = "Copy", command=copy, font=("Arial", 14))
    EditMenu.add_command(label = "Paste", command=paste, font=("Arial", 14))
    EditMenu.add_command(label = "PDF CONVERTER", command=pdf_converter(), font=("Arial", 14))
    # EditMenu.add_command(label = "Find", command=find, font=("Arial", 14))

    MenuBar.add_cascade(label="Edit", menu = EditMenu, font=("Arial", 20))

    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about, font=("Arial", 14))
    MenuBar.add_cascade(label="Help", menu=HelpMenu, font=("Arial", 20))

    # Help Menu Ends

    root.config(menu=MenuBar)

    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()

#END OF PROJECT