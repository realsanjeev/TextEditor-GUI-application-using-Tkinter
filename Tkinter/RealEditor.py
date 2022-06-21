from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from tkinter.ttk import Labelframe
from turtle import undo

class realMenu(Menu):
    def __init__(self, master):
        Menu.__init__(self, master)
        fileMenu = Menu(self, tearoff='off')
        mainMenu.add_cascade(label = 'File', menu = fileMenu)
        fileMenu.add_command(label = 'New', command=getNewFile)
        fileMenu.add_command(label='Open', command=getOpenFile)
        fileMenu.add_separator()
        fileMenu.add_command(label='Save As', command=getSaveAsFile)
        fileMenu.add_command(label='Save', command=getSaveFile)
        fileMenu.add_command(label='Exit', command=getExitFile)

        editMenu = Menu(mainMenu, tearoff='off')
        mainMenu.add_cascade(label='Edit', menu = editMenu)
        editMenu.add_command(label='Undo', command= getUndoEdit)
        editMenu.add_command(label='Redo', command= getRedoEdit)
        editMenu.add_separator()
        editMenu.add_command(label='Cut', command=getCut, compound='right')
        editMenu.add_command(label='Copy', command=getCopy)
        editMenu.add_separator()
        editMenu.add_command(label='Find', command=getFindEdit)
        editMenu.add_command(label='Replace', command=getReplaceEdit)

        viewMenu = Menu(mainMenu, tearoff='off')
        mainMenu.add_cascade(label='View', menu = viewMenu)
        viewMenu.add_command(label='Status Bar', command=get)

        helpMenu = Menu(mainMenu, tearoff='off')
        mainMenu.add_cascade(label='View', menu = helpMenu)
        helpMenu.add_command(label='About', command=getAboutEditor, bitmap="questhead", compound='left')
        helpMenu.add_command(label='Helps', command=getAboutEditor, bitmap="question", compound='left')




root = Tk(screenName='Real Text Editor')
root.wm_title('Real Text Editor')
root.wm_iconbitmap('computer.ico')
root.wm_geometry('340x220')

editingFrame = Frame(root)
editingFrame.pack(fill='both', expand=-1)

labelFrame=Frame(root)
labelFrame.pack(side='bottom')

mainMenu = Menu(root)
root.config(menu = mainMenu)

def getNewFile():
    global file
    file = None
    root.title("Untitled - Real Text Editor")
    textEditor.delete(1.0, END)

def getOpenFile():
    fileExt= [('All files','*.*'),('Text Document','*.txt')]
    f=fd.askopenfile(filetypes=fileExt, 
        defaultextension=('Text File',('*,txt')), title='Open File in Real Text Editor')
    if f is not None:
        content=f.read()
        print(content)
    textEditor.insert('1.0', content)
    print(f)
    root.wm_title(f)

def getSaveAsFile():
    fileExt= [('All files','*.*'),('Text Document','*.txt')]
    fileName = fd.asksaveasfile(initialfile='untitled.txt', defaultextension='.txt',filetypes=fileExt)
    try:
        with open(fileName, 'w') as f:
            contents = textEditor.get(1.0, END)
            f.write(contents)

    except FileNotFoundError:
        return 'cancelled'

def getSaveFile():
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

            root.title(os.path.basename(file) + " - Real Text Editor")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textEditor.get(1.0, END))
        f.close()

def getExitFile(event=None):
    root.destroy()

    print('ok')

def get():
    print('ok')

def getUndoEdit(event=None):
    textEditor.event_generate(("<Undo>"))

def getRedoEdit(event=None):
    textEditor.event_generate(("<Redo>"))

def getFindEdit():

    # to create a window
    rfind = Tk()

    # rfind window is the parent window
    fram = Frame(rfind)

    # Creating Label, Entry Box, Button
    # and packing them adding label to
    # search box
    Label(fram, text ='Find').pack(side = LEFT)

    # adding of single line text box
    edit = Entry(fram)

    # positioning of text box
    edit.pack(side = LEFT, fill = BOTH, expand = 1)

    # setting focus
    edit.focus_set()

    # adding of search button
    Find = Button(fram, text ='Find')
    Find.pack(side = LEFT)


    Label(fram, text = "Replace With ").pack(side = LEFT)

    edit2 = Entry(fram)
    edit2.pack(side = LEFT, fill = BOTH, expand = 1)
    edit2.focus_set()

    replace = Button(fram, text = 'FindNReplace')
    replace.pack(side = LEFT)

    fram.pack(side = TOP)

    # function to search string in text
    def find():
        
        # remove tag 'found' from index 1 to END
        textEditor.tag_remove('found', '1.0', END)
        
        # returns to widget currently in focus
        s = edit.get()
        
        if (s):
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = textEditor.search(s, idx, nocase = 1, stopindex = END)
                
                if not idx: break
                
                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(s))
                

                # overwrite 'Found' at idx
                textEditor.tag_add('found', idx, lastidx)
                idx = lastidx

                # mark located string as red
            textEditor.tag_config('found', foreground ='red')
        edit.focus_set()

    def findNreplace():
        
        # remove tag 'found' from index 1 to END
        textEditor.tag_remove('found', '1.0', END)
        
        # returns to widget currently in focus
        s = edit.get()
        r = edit2.get()
        
        if (s and r):
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = textEditor.search(s, idx, nocase = 1,
                                stopindex = END)
                print(idx)
                if not idx: break
                
                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(s))

                textEditor.delete(idx, lastidx)
                textEditor.insert(idx, r)

                lastidx = '% s+% dc' % (idx, len(r))
                
                # overwrite 'Found' at idx
                textEditor.tag_add('found', idx, lastidx)
                idx = lastidx

            # mark located string as red
            textEditor.tag_config('found', foreground ='green', background = 'yellow')
        edit.focus_set()

                    
    Find.config(command = find)
    replace.config(command = findNreplace)

    # mainloop function calls the endless
    # loop of the window, so the window will
    # wait for any user interaction till we
    # close it


def getReplaceEdit():
    print('ok')

def getSelectAllView():
    pass

def getCopy(event=None):
    textEditor.event_generate(("<Copy>"))

def getCut(event=None):
    textEditor.event_generate(("<Cut>"))

def getAboutEditor():
    msg='''This is Real Text Editor. Real Text Editor is developed by Real Sanjeev.
    Develop for educational purpose. 
    '''
    showinfo(title='About Real Text Editor', message=msg.pack())


textEditor=Text(editingFrame)
textEditor.pack(fill='both', expand=True)

yscrollbar = Scrollbar(textEditor, orient='vertical')
yscrollbar.pack(side=RIGHT, fill='y')

xscrollbar = Scrollbar(textEditor, orient='horizontal')
xscrollbar.pack(side=BOTTOM, fill='x')

textEditor.config(yscrollcommand=yscrollbar.set, state='normal', xscrollcommand=xscrollbar.set,
                        undo=True, endline=5)

lb=Label(labelFrame, text='Line no')
lb.pack(side='right', expand=1)

root.bind('<Control-s>',getSaveFile)
root.bind('<Control-S>',getSaveFile)
root.bind('<Control-x>',getExitFile)
root.bind('<Control-Y>',getExitFile)
root.bind('<Control-A>', getSelectAllView)

if __name__=='__main__':
    realMenu(mainMenu)
    root.mainloop()