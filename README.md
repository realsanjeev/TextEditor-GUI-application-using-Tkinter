# RealTextEditor-GUI-desktop-application-using-Tkinter

The project is a module that creates a text editor using tkinter GUI. It imports necessary classes and methods from tkinter for GUI creation. The module defines several classes, such as **Tk, Menu, Frame, Button, Toplevel, Label, Text, Entry, ttk, showinfo, askquestion, fd, and asksaveasfilename**. It also defines a function getAboutEditor to get the about information for the text editor.

The main program creates an instance of the Tk class and sets the window title, icon, and geometry. It also defines a global variable FILE that stores the file name to be opened, edited, or saved.

The module defines a `RealMenu` class that represents a customized menu. The `RealMenu` class inherits from the Menu class and initializes a new instance of the Menu class with the parent object that the menu belongs to. The `RealMenu` class creates a file menu with commands to create a new file, open an existing file, save the file, and exit the application. It also creates an edit menu with commands to undo, redo, cut, copy, find, and replace the text. The `RealMenu` class creates a view menu with a command to show or hide the status bar. Finally, it creates a help menu with commands to show the about information and the help documentation.

The `get_find_edit` method of the `RealMenu` class creates a top-level window to find and replace the text in the text editor. The method creates a frame with a label, an entry box, a button, and a label, an entry box, and a button for the replace text. The find button invokes a function to search for the desired string from index 1. It then highlights the found text in the text editor. If the text is not found, it shows a message box.

**It tries to immitate Notepad**

### References:
- [Creating GUI](https://www.pythonguis.com/tutorials/create-gui-tkinter/)

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to submit a pull request.

## Contact Me

<table>
  <tr>
    <td><img src="https://github.com/realsanjeev/protfolio/blob/main/src/assets/images/instagram.png" alt="Instagram" width="50" height="50"></td>
    <td><img src="https://github.com/realsanjeev/protfolio/blob/main/src/assets/images/twitter.png" alt="Twitter" width="50" height="50"></td>
    <td><img src="https://github.com/realsanjeev/protfolio/blob/main/src/assets/images/github.png" alt="GitHub" width="50" height="50"></td>
    <td><img src="https://github.com/realsanjeev/protfolio/blob/main/src/assets/images/linkedin-logo.png" alt="LinkedIn" width="50" height="50"></td>
  </tr>
</table>
