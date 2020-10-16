booklist = """Genesis
Exodus
Leviticus
Numbers
Deuteronomy
Joshua
Judges
Ruth
1 Samuel
2 Samuel
1 Kings
2 Kings
1 Chronicles
2 Chronicles
Ezra
Nehemiah
Esther
Job
Psalm
Proverbs
Ecclesiastes
Song of Solomon
Isaiah
Jeremiah
Lamentations
Ezekiel
Daniel
Hosea
Joel
Amos
Obadiah
Jonah
Micah
Nahum
Habakkuk
Zephaniah
Haggai
Zechariah
Malachi
Matthew
Mark
Luke
John
Acts
Romans
1 Corinthians
2 Corinthians
Galatians
Ephesians
Philippians
Colossians
1 Thessalonians
2 Thessalonians
1 Timothy
2 Timothy
Titus
Philemon
Hebrews
James
1 Peter
2 Peter
1 John
2 John
3 John
Jude
Revelation""".split("\n")

FOLDERPATH = "/Users/xcelchurchdarlington/Documents/TestScriptures/"
import sys


import os

from tkinter import *
root =  Tk()
root.title("Delete Scriptures")
root.lift()
root.attributes("-topmost", True)

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__()
        self.pack()
        self.scriptureList = []
        self.addObjs()
        self.update()
        
    def addObjs(self):
        self.delBut = Button(self,text="Delete All Certain Scriptures")
        self.delBut.grid(column=0,row=0,sticky=W+E+N+S)
        self.updBut = Button(self,text="Update",command=self.update)
        self.updBut.grid(column=1,row=0,sticky=W+E+N+S)
        self.desBut = Button(self, text="Deselect all")
        self.desBut.grid(column=0,row=1,sticky=W+E+N+S)
        self.selBut = Button(self, text="Select all")
        self.selBut.grid(column=1,row=1,sticky=W+E+N+S)
        self.filFrm = Frame(self)
        self.filFrm.grid(column=0,row=20,columnspan=2)
        self.filLib = Listbox(self.filFrm)
        self.filLib.pack(side="left",fill="y")       
        self.filScr = Scrollbar(self.filFrm, orient="vertical")
        self.filScr.pack(side="right", fill="y")
        self.filLib.config(yscrollcommand=self.filScr.set)
        self.filLib.bind("<Double-Button-1>", self.onDouble)
    def onDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = selection[0]
        self.toggle(value)
    def toggle(self, fn):
        print(self.scriptureList[fn].filename,fn,self.scriptureList[fn].scripture,self.scriptureList[fn].uncertain)
    def update(self):
        stray = 0
        self.len_max = 1
        global FOLDERPATH
        self.scriptureList = [] # empty the list
        for fn in os.listdir(FOLDERPATH):  # list all file names in folder
                self.scriptureList.append(Scripture(fn)) # add scripture objects to list, passing them the filename
        i =0
        while i < len(self.scriptureList):
            scriptureObj = self.scriptureList[i]
            if not scriptureObj.scripture or not scriptureObj.uncertain:
                print(self.scriptureList[i].filename)
                del self.scriptureList[i]
                i=i-1
            i=i+1
        for index,scriptureObj in enumerate(self.scriptureList):
            
            self.filLib.insert(END,scriptureObj.filename)
                
            if len(scriptureObj.filename) > self.len_max:
                self.len_max = len(scriptureObj.filename)
            if scriptureObj.scripture:
                self.filLib.itemconfig(index, {'fg': 'blue'})
            elif scriptureObj.uncertain:
                self.filLib.itemconfig(index, {'fg': 'orange'})

        self.filLib["width"] = self.len_max
"""
class ScriptureListFrm(Frame):
    def __init__(self, master):
        super(ScriptureList, self).__init__()
        self.pack()
        self.addObjs()
    def addObjs(self):
        
 """       


class Scripture():
    def __init__(self, fn):
        self.filename = fn
        self.bookInFilename = False
        self.inBibleCategory = False
        self.scripture = False
        self.uncertain = False
        if ".pro6" in self.filename:
            self.ppFile = True
            global FOLDERPATH
            self.filePath = str(FOLDERPATH+self.filename)
            #print(self.filePath)
            global booklist
            for book in booklist:
                if book in self.filename:
                    self.bookInFilename = True
                    
            x = open(self.filePath,"r").read()
            if """category="Bible" """ in x:
                self.inBibleCategory = True
            
        else:
            self.ppFile = False

        if self.bookInFilename and self.inBibleCategory:
            self.scripture = True
        elif self.bookInFilename != self.inBibleCategory:
            self.uncertain = True
            
        

        
        
"""
for filename in os.listdir("/Users/xcelchurchdarlington/Documents/ProPresenter6"):
    for item in books:
        if item in filename:
            filegoto = str("/Users/xcelchurchdarlington/Documents/ProPresenter6/"+filename)
            print(filegoto)
            if """#category="Bible" """ in open(filegoto,"r").read():
#                os.remove(filegoto)

#5"""


app = Application(root)
root.mainloop()



    
