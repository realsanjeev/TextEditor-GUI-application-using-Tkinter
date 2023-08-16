"""
Module to create a text editor using tkinter GUI.

This module imports necessary classes and methods from tkinter for GUI creation.
Classes:

Tk: The main tkinter window.
Menu: The tkinter menu.
Frame: The tkinter frame for widgets.
Button: The tkinter button.
Toplevel: The tkinter toplevel window.
Label: The tkinter label.
Text: The tkinter text widget.
Entry: The tkinter entry widget.
ttk: The tkinter themed widgets.
showinfo: The tkinter messagebox to display information.
askquestion: The tkinter messagebox to ask question.
fd: The tkinter filedialog for open and save.
asksaveasfilename: The tkinter filedialog to save files.
getAboutEditor: A function to get the about information for the text editor.
Functions:
"""

from tkinter import Tk, Menu, Frame, Button, Toplevel
from tkinter import Label, Text, Entry
from tkinter import ttk
from tkinter.messagebox import showinfo, askquestion
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfilename
from view import getAboutEditor, display_in_console

root = Tk(screenName='Real Text Editor')
root.wm_title('Real Text Editor')
root.wm_iconbitmap('computer.ico')
root.wm_geometry('340x220')

FILE = None

class RealMenu(Menu):
    """A class representing a customized menu.

    Attributes:
        counter (int): A class attribute to keep track of the number of instances.
        msg (str): A class attribute representing the creation message.

    Args:
        master (obj): The parent object that the menu belongs to.
    """
    counter = 0
    msg='''This is real's Creation'''

    def __init__(self, master):
        """
        Initializes a new instance of the RealMenu class.

        Args:
            master (obj): The parent object that the menu belongs to.
        """
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
        edit_menu.add_command(label='Replace', command=self.get_find_edit)

        view_menu = Menu(mainMenu, tearoff='off')
        mainMenu.add_cascade(label='View', menu = view_menu)
        view_menu.add_command(label='Status Bar', command=get)

        help_menu = Menu(mainMenu, tearoff='off')
        mainMenu.add_cascade(label='Help', menu = help_menu)
        help_menu.add_command(label='About', command=getAboutEditor,
                                    bitmap="questhead", compound='left')
        help_menu.add_command(label='Helps', command=getAboutEditor,
                                    bitmap="question", compound='left')

    def get_find_edit(self):
        '''Function to open a child window for find and replace operations.'''

        child_window = Toplevel(self)
        child_window.wm_iconbitmap('search.ico')

        search_frame = Frame(child_window)

        # Creating Label, Entry Boxes, and Buttons for Find and Replace
        Label(search_frame, text='Find').pack(side='left')
        edit = Entry(search_frame)
        edit.pack(side='left', fill='both', expand=1)
        edit.focus_set()

        find_btn = Button(search_frame, text='Find', command=lambda: find(edit))
        find_btn.pack(side='left')

        Label(search_frame, text='Replace With ').pack(side='left')
        edit2 = Entry(search_frame)
        edit2.pack(side='left', fill='both', expand=1)
        edit2.focus_set()

        replace_btn = Button(search_frame, text='Replace', command=lambda: find_and_replace(edit, edit2))
        replace_btn.pack(side='left')

        search_frame.pack(side='top')

def find(edit):
    '''Function to find and highlight occurrences of the search text.'''
    text_editor.tag_remove('found', '1.0', 'end')

    search = edit.get()
    if search:
        idx = '1.0'
        while True:
            idx = text_editor.search(search, idx, nocase=1, stopindex='end')
            if not idx:
                break
            lastidx = f'{idx} + {len(search)}c'

            text_editor.tag_add('found', idx, lastidx)
            idx = lastidx

        text_editor.tag_config('found', foreground='red')

def find_and_replace(edit, edit2):
    '''Function to find and replace occurrences of the search text with replacement.'''
    text_editor.tag_remove('found', '1.0', 'end')

    search = edit.get()
    replace = edit2.get()

    if search and replace:
        idx = '1.0'
        while True:
            idx = text_editor.search(search, idx, nocase=1, stopindex='end')
            if not idx:
                break
            lastidx = f'{idx} + {len(search)}c'

            text_editor.delete(idx, lastidx)
            text_editor.insert(idx, replace)

            text_editor.tag_add('found', idx, lastidx)
            idx = lastidx

        text_editor.tag_config('found', foreground='green', background='yellow')


def get_new_file():
    """
    Clears the text editor and sets the title to 'Untitled - Real Text Editor'.
    """
    if file is not None:
        file = None
    root.wm_title("Untitled - Real Text Editor")
    text_editor.delete(1.0, 'end-1c')

def get_open_file():
    '''
    Open a dialog box to select a text-only file, such as .py, .txt, or .c extension,
    to be opened in Real Text Editor.
    '''
    file_ext = [('All files', '*.*'),
                ('Text Document', '*.txt')]
    file_name = fd.askopenfile(filetypes=file_ext, 
                            defaultextension=('Text File',('*,txt')),
                            title='Open File in Real Text Editor')
    if file_name is not None:
        content = file_name.read()
        text_editor.delete(1.0, 'end') 
        text_editor.insert('1.0', content) 
        display_in_console(f'Type of content: {type(content)} and file_name: {file_name}')
        title = file_name.name.split('/') 
        display_in_console(f'file name: {title[-1]} and filetype: {type(file_name)}')

        root.wm_title('Real Text Editor - ' + title[-1])


def get_save_as_file():
    """
    Open a dialog box to save the file with the chosen name and format.

    Returns:
        If file is not saved: returns 'cancelled'.
    """
    file_ext = [('All files','*.*'),
                ('Text Document','*.txt')]
    file_name = fd.asksaveasfile(initialfile='untitled.txt',
                                    defaultextension='.txt', 
                                    confirmoverwrite=True,
                                    filetypes=file_ext)
    try:
        with open(file_name.name, 'wb') as file_save_name:
            contents = text_editor.get("1.0","end-1c")
            file_save_name.write(bytes(contents, 'cp1252'))
    except FileNotFoundError:
        return 'cancelled'


def get_save_file():
    '''
    Save the content to an existing file or save as a new file.
    '''
    file_ext = [("All Files", "*.*"), 
                ("Text Documents", "*.txt")]
    if FILE is None:
        file = asksaveasfilename(initialfile='Untitled.txt', 
                                defaultextension=".txt",
                                filetypes=file_ext)
        if file =="":
            file = None
        else:
            #Save as a new file
            with open(file.name, 'w') as file_save_name:
                contents = text_editor.get("1.0","end-1c")
                file_save_name.write(bytes(contents, 'cp1252'))

            root.wm_title(file + " - Real Text Editor")
            display_in_console("File Saved")
    else:
        # Save the file
        with open(file, "w", encoding='cp1252') as file_p:
            file_p.write(text_editor.get(1.0, 'end-1c'))

def get_exit_file():
    '''
    This function prompts the user to save changes before closing the application window.
    If the user clicks "Yes", the changes are saved and the application window is closed.
    If the user clicks "No", the application window is closed without saving changes.
    '''
    if FILE is None:
        option = askquestion(title='Save CURRENT file', message='Save Or Quit')
        display_in_console(option)
        if option:
            get_save_file()
    root.destroy()

    display_in_console('ok')


def get():
    '''get function'''
    display_in_console('ok')

def get_undo_edit():
    """
    Generates an event for the text editor to perform undo operation.
    """
    text_editor.event_generate(("<Undo>"))

def get_redo_edit():
    """
    Generates an event for the text editor to perform redo operation.
    """
    text_editor.event_generate(("<Redo>"))

def get_copy():
    """
    Generates an event for the text editor to copy the selected text.
    """
    text_editor.event_generate(("<Copy>"))


def get_select_all_view():
    display_in_console('Selceted All View')

def get_cut():
    '''cut function'''
    text_editor.event_generate(("<Cut>"))

editing_frame = Frame(root)
editing_frame.pack(fill='both', expand=1)

labelFrame=Frame(root)
labelFrame.pack(side='bottom')

mainMenu = Menu(root)
root.config(menu=mainMenu)

text_editor=Text(editing_frame, padx=3, pady=2, 
                        wrap='none', maxundo=10,
                        undo=True, blockcursor=True, autoseparators=True)
text_editor.pack(anchor='nw', fill='both', expand='1', padx=1, pady=2)

yscrollbar = ttk.Scrollbar(text_editor, orient='vertical',
                            cursor='arrow', command=text_editor.yview,)
yscrollbar.pack(side='right', fill='y')

xscrollbar = ttk.Scrollbar(text_editor, orient='horizontal',
                           cursor='arrow', command=text_editor.xview)
xscrollbar.pack(side='bottom', fill='x')

#  communicate back to the scrollbar
text_editor['yscrollcommand'] = yscrollbar.set
text_editor['xscrollcommand'] = xscrollbar.set

# text_editor.config( background='red',
#                     yscrollcommand=yscrollbar.set, 
#                     state='normal', 
#                     xscrollcommand=xscrollbar.set,
#                     tabstyle='tabular',
#                     undo=True, 
#                     endline=5
#                     )

lb=Label(labelFrame, text='REALTEXT')
lb.pack(side='right', expand=1)



if __name__=='__main__':
    RealMenu(mainMenu)
    root.bind('<Control-s>',get_save_file)
    root.bind('<Control-S>',get_save_file)
    root.bind('<Control-x>',get_exit_file)
    root.bind('<Control-X>',get_exit_file)
    root.mainloop()
