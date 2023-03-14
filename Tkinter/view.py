from tkinter.messagebox import showinfo

def getAboutEditor():
    """
    Display an about message box with information about Real Text Editor.

    Returns:
        None
    """
    msg='''
    This is Real Text Editor. Real Text Editor is developed by Real Sanjeev.
    This project is made using tkinter python GNU Liabiries. Most of program is procedural programing method rather than objet oriented approach. It is easy to understand program

    Develop for educational purpose. 
    '''
    showinfo(title='About Real Text Editor', message=msg)
