import tkinter.messagebox as messagebox

def getAboutEditor():
    """
    Display an about message box with information about Real Text Editor.

    Returns:
        None
    """
    msg = '''\
    This is Real Text Editor. 
    
    Real Text Editor is developed by Real Sanjeev.
    This project is made using tkinter python GNU Libraries. Most of the program uses a procedural programming method rather than an object-oriented approach. It is easy to understand the program.

    Developed for educational purposes.
    '''
    messagebox.showinfo(
        title='About Real Text Editor',
        message=msg,
        icon=messagebox.INFO,
        type=messagebox.OK
    )

def display_in_console(str):
    print("*"*30)
    print(str)
    print("*"*30)