import os
from tkinter import (Tk, Menu, Frame, Button, Toplevel,
                     Label, Text, Entry, ttk,
                     filedialog as fd)
from tkinter.messagebox import askquestion, showinfo
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk

from src.view import getAboutEditor, display_in_console

root = Tk()
root.wm_title('Real Text Editor')
root.configure(background="red")

# Icon of the app
im = Image.open('images/computer.ico')
photo = ImageTk.PhotoImage(im)
root.wm_iconphoto(True, photo)

# set a minimum window size (width, height)
root.minsize(500, 400)
root.geometry('1600x900')


FILE = None

class RealMenu(Menu):
    def __init__(self, master):
        super().__init__(master)
        
        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(label='New', command=get_new_file)
        file_menu.add_command(label='Open', command=get_open_file)
        file_menu.add_separator()
        file_menu.add_command(label='Save As', command=get_save_as_file)
        file_menu.add_command(label='Save', command=get_save_file)
        file_menu.add_command(label='Exit', command=get_exit_file)
        self.add_cascade(label='File', menu=file_menu)
        
        edit_menu = Menu(self, tearoff=0)
        edit_menu.add_command(label='Undo', command=get_undo_edit)
        edit_menu.add_command(label='Redo', command=get_redo_edit)
        edit_menu.add_separator()
        edit_menu.add_command(label='Cut', command=get_cut)
        edit_menu.add_command(label='Copy', command=get_copy)
        edit_menu.add_command(label='Paste', command=get_paste)
        edit_menu.add_separator()
        edit_menu.add_command(label='Find', command=self.get_find_edit)
        edit_menu.add_command(label='Replace', command=self.get_find_edit)
        self.add_cascade(label='Edit', menu=edit_menu)
        
        view_menu = Menu(self, tearoff=0)
        view_menu.add_command(label='Status Bar', command=get_status_bar)
        self.add_cascade(label='View', menu=view_menu)
        
        help_menu = Menu(self, tearoff=0)
        help_menu.add_command(label='About', command=getAboutEditor)
        help_menu.add_command(label='Help', command=lambda: showinfo('Help', 'Use the menu options to edit text.'))
        self.add_cascade(label='Help', menu=help_menu)
        
        master.config(menu=self)

    def get_find_edit(self):
        child_window = Toplevel(self)
        child_window.title("Find and Replace")
        
        Label(child_window, text='Find').grid(row=0, column=0)
        find_entry = Entry(child_window)
        find_entry.grid(row=0, column=1)
        
        Label(child_window, text='Replace With').grid(row=1, column=0)
        replace_entry = Entry(child_window)
        replace_entry.grid(row=1, column=1)
        
        Button(child_window, text='Find', command=lambda: find(find_entry)).grid(row=0, column=2)
        Button(child_window, text='Replace', command=lambda: find_and_replace(find_entry, replace_entry)).grid(row=1, column=2)

def find(edit):
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
    search, replace = edit.get(), edit2.get()
    if search and replace:
        text_content = text_editor.get('1.0', 'end-1c')
        new_content = text_content.replace(search, replace)
        text_editor.delete('1.0', 'end')
        text_editor.insert('1.0', new_content)

def get_new_file():
    global FILE
    FILE = None
    root.title("Untitled - Real Text Editor")
    text_editor.delete(1.0, 'end')

def get_open_file():
    file_path = fd.askopenfilename(filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if file_path:
        with open(file_path, 'r') as file:
            text_editor.delete(1.0, 'end')
            text_editor.insert('1.0', file.read())
        root.title(f'Real Text Editor - {os.path.basename(file_path)}')

def get_save_as_file():
    file_path = asksaveasfilename(filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_editor.get('1.0', 'end-1c'))
        root.title(f'Real Text Editor - {os.path.basename(file_path)}')

def get_save_file():
    global FILE
    if FILE:
        with open(FILE, 'w') as file:
            file.write(text_editor.get('1.0', 'end-1c'))
    else:
        get_save_as_file()

def get_exit_file():
    if askquestion('Exit', 'Save changes before quitting?') == 'yes':
        get_save_file()
    root.quit()

def update_status(event=None, status_bar=None):
    """Updates the status bar with current line, column, and total lines."""
    total_lines = int(text_editor.index('end-1c').split('.')[0])  # Total number of lines
    line, col = text_editor.index('insert').split('.')  # Get current cursor position

    # Update filename if available
    filename_display = FILE if FILE else "Untitled"

    # Update the status bar
    status_bar.config(text=f"{filename_display} | Line {line}, Col {col} | Total Lines: {total_lines}")

def get_status_bar():
    status_bar = Label(root, text="Ready", anchor="w", relief="sunken", bd=1, padx=5)
    status_bar.grid(row=1, column=0, columnspan=2, sticky="ew")

    # Bind events to update status dynamically, passing status_bar as argument
    text_editor.bind('<KeyRelease>', lambda event: update_status(event, status_bar))
    text_editor.bind('<ButtonRelease>', lambda event: update_status(event, status_bar))

def get_undo_edit():
    text_editor.edit_undo()

def get_redo_edit():
    text_editor.edit_redo()

def get_copy():
    text_editor.event_generate("<<Copy>>")

def get_cut():
    text_editor.event_generate("<<Cut>>")

def get_paste():
    text_editor.event_generate("<<Paste>>")

def get_select_all():
    text_editor.event_generate("<<SelectAll>>")

# GUI Components
text_editor = Text(root, wrap='word', undo=True)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=text_editor.yview)

# Attach scrollbar to text widget
text_editor.config(yscrollcommand=scrollbar.set)

# Use grid for better placement
text_editor.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Configure root window grid to allow resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# bind the select all functionality
root.bind("<Control-a>", lambda event: get_select_all())
root.bind("<Control-A>", lambda event: get_select_all())


main_menu = RealMenu(root)

if __name__ == '__main__':
    root.mainloop()
