'''importing tkinter different class and method'''
from tkinter import Tk, Menu, Frame, Button, Toplevel
from tkinter import Label, Scrollbar, END, LEFT, BOTH, BOTTOM, TOP, RIGHT, Text, Entry
from tkinter.messagebox import showinfo,  askquestion
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfilename
from view import getAboutEditor

root = Tk(screenName='Real Text Editor')
root.wm_title('Real Text Editor')
root.wm_iconbitmap('editorIcon.ico')
root.wm_geometry('340x220')

FILE = None

class RealMenu(Menu):
    '''Making menu class'''
    counter = 0
    msg='''This is real's Creation'''
    def __init__(self, master):
        Menu.__init__(self, master)
        file_menu = Menu(self, tearoff='off')
        mainMenu.add_cascade(label = 'File', menu = file_menu)
        file_menu.add_command(label = 'New', command=get_new_file)
        file_menu.add_command(label='Open', command=get_open_file)
        file_menu.add_separator()
        file_menu.add_command(label='Save As', command=get_save_as_file)
        file_menu.add_command(label='Save', command=get_save_file)
        file_menu.add_command(label='Exit', command=get_exit_file)

        edit_menu = Menu(mainMenu, tearoff='off')
        mainMenu.add_cascade(label='Edit', menu = edit_menu)
        edit_menu.add_command(label='Undo', command= get_undo_edit)
        edit_menu.add_command(label='Redo', command= get_redo_edit)
        edit_menu.add_separator()
        edit_menu.add_command(label='Cut', command=get_cut, compound='right')
        edit_menu.add_command(label='Copy', command=get_copy)
        edit_menu.add_separator()
        edit_menu.add_command(label='Find', command=self.get_find_edit)
        edit_menu.add_command(label='Replace', command=get_replace_edit)

        view_menu = Menu(mainMenu, tearoff='off')
        mainMenu.add_cascade(label='View', menu = view_menu)
        view_menu.add_command(label='Status Bar', command=get)

        help_menu = Menu(mainMenu, tearoff='off')
        mainMenu.add_cascade(label='View', menu = help_menu)
        help_menu.add_command(label='About', command=getAboutEditor,
                                    bitmap="questhead", compound='left')
        help_menu.add_command(label='Helps', command=getAboutEditor,
                                    bitmap="question", compound='left')

    def get_find_edit(self):
        '''for find edit function'''
        self.counter += 1

        if self.counter > 1:
            self.msg='''Please you already have find and replace opened.
                '''
            showinfo(title='Error', message=self.msg)
            return
        # to only open one window for find and replace

        rfind = Toplevel(self)
        rfind.wm_iconbitmap('search.ico')
        # rfind window is the parent window
        fram = Frame(rfind)

        # Creating Label, Entry Box, Button and packing them adding label tosearch box
        Label(fram, text ='Find').pack(side = LEFT)

        # adding of single line text box
        edit = Entry(fram)

        # positioning of text box
        edit.pack(side = LEFT, fill = BOTH, expand = 1)

        # setting focus
        edit.focus_set()

        # adding of search button
        find_b = Button(fram, text ='Find')
        find_b.pack(side = LEFT)

        Label(fram, text = "Replace With ").pack(side = LEFT)

        edit2 = Entry(fram)
        edit2.pack(side = LEFT, fill = BOTH, expand = 1)
        edit2.focus_set()

        replace = Button(fram, text = 'Replace')
        replace.pack(side = LEFT)

        fram.pack(side = TOP)

        # function to search string in text
        def find():
            # remove tag 'found' from index 1 to END
            textEditor.tag_remove('found', '1.0', END)
            # returns to widget currently in focus
            search = edit.get()
            if search:
                idx = '1.0'
                while 1:
                    # searches for desired string from index 1
                    idx = textEditor.search(search, idx, nocase = 1, stopindex = END)
                    if not idx:
                        break
                    # last index sum of current index and
                    # length of text
                    lastidx = f'{idx} + {len(search)}'

                    # overwrite 'Found' at idx
                    textEditor.tag_add('found', idx, lastidx)
                    idx = lastidx

                    # mark located string as red
                textEditor.tag_config('found', foreground ='red')
            edit.focus_set()

        def find_n_replace():
            # remove tag 'found' from index 1 to END
            textEditor.tag_remove('found', '1.0', END)
            # returns to widget currently in focus
            search = edit.get()
            replace = edit2.get()
            if (search and replace):
                idx = '1.0'
                while 1:
                    # searches for desired string from index 1
                    idx = textEditor.search(search, idx, nocase = 1,
                                    stopindex = END)
                    print(idx)
                    if not idx:
                        break
                    # last index sum of current index and
                    # length of text
                    lastidx = f'{idx} + {len(search)}'

                    textEditor.delete(idx, lastidx)
                    textEditor.insert(idx, replace)

                    lastidx = f'{idx} + {len(search)}'
                    # overwrite 'Found' at idx
                    textEditor.tag_add('found', idx, lastidx)
                    idx = lastidx

                # mark located string as red
                textEditor.tag_config('found', foreground ='green', background = 'yellow')
            edit.focus_set()

        find_b.config(command = find)
        replace.config(command = find_n_replace)

def get_new_file():
    '''for new file function'''
    if file is not None:
        file = None
    root.title("Untitled - Real Text Editor")
    textEditor.delete(1.0, END)

def get_open_file():
    '''for open file function'''
    file_ext= [('All files','*.*'),('Text Document','*.txt')]
    file_name=fd.askopenfile(filetypes=file_ext, defaultextension=('Text File',('*,txt')),
                        title='Open File in Real Text Editor')
    if file_name is not None:
        content=file_name.read()
        print(content)
        textEditor.insert('1.0', content)
        print(file_name)
        root.wm_title(file_name)

def get_save_as_file():
    '''for save as file menu function'''
    file_ext= [('All files','*.*'),('Text Document','*.txt')]
    file_name = fd.asksaveasfile(initialfile='untitled.txt',
                                    defaultextension='.txt', filetypes=file_ext)
    try:
        with open(file_name.name, 'w', encoding='utf-16') as file_p:
            contents = textEditor.get("1.0","end-1c")
            file_p.write(contents)

    except FileNotFoundError:
        return 'cancelled'

def get_save_file():
    '''for save option function'''
    if FILE is None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file =="":
            file = None
        else:
            #Save as a new file
            with open(file.name, 'w', encoding='utf-16') as file_p:
                contents = textEditor.get("1.0","end-1c")
                file_p.write(contents)

            root.title(file + " - Real Text Editor")
            print("File Saved")
    else:
        # Save the file
        with open(file, "w", encoding='utf-16') as file_p:
            file_p.write(textEditor.get(1.0, END))

def get_exit_file():
    '''for exit function of window'''
    if FILE is None:
        option = askquestion(title='Save CURRENT file', message='Save Or Quit')
        print(option)
        if option:
            get_save_file()
    root.destroy()

    print('ok')

def get():
    '''get function'''
    print('ok')

def get_undo_edit():
    '''get undo edit function'''
    textEditor.event_generate(("<Undo>"))

def get_redo_edit():
    '''get redo edit'''
    textEditor.event_generate(("<Redo>"))

def get_replace_edit():
    '''get replace edit function'''
    print('ok')

def get_select_all_view():
    '''selct all function'''
    print('ok')

def get_copy():
    '''copy function'''
    textEditor.event_generate(("<Copy>"))

def get_cut():
    '''cut function'''
    textEditor.event_generate(("<Cut>"))

editingFrame = Frame(root)
editingFrame.pack(fill='both', expand=-1)

labelFrame=Frame(root)
labelFrame.pack(side='bottom')

mainMenu = Menu(root)
root.config(menu = mainMenu)

textEditor=Text(editingFrame)
textEditor.pack(fill='both', expand=True)

yscrollbar = Scrollbar(textEditor, orient='vertical')
yscrollbar.pack(side=RIGHT, fill='y')

xscrollbar = Scrollbar(textEditor, orient='horizontal')
xscrollbar.pack(side=BOTTOM, fill='x')

textEditor.config(yscrollcommand=yscrollbar.set, state='normal', xscrollcommand=xscrollbar.set,
                        undo=True, endline=5)

lb=Label(labelFrame, text='REALTEXT')
lb.pack(side='right', expand=1)



if __name__=='__main__':
    RealMenu(mainMenu)
    root.bind('<Control-s>',get_save_file)
    root.bind('<Control-S>',get_save_file)
    root.bind('<Control-x>',get_exit_file)
    root.bind('<Control-X>',get_exit_file)
    root.mainloop()
