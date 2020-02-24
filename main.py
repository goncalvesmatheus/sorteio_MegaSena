# ================= #
# === Interface === #
# ================= #
from tkinter import *
from tkinter import messagebox
from sorteio import *
import sorteio
import webbrowser
import urllib.parse

s = MyClass()


# Function to close the application.
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


# Function to show informations About
def aboutInf():
    messagebox.showinfo(
        "About", "\nVersion 2.0\nDeveloped by\nMatheus Gonçalves")


# Function sending for the URL project
def projectURL():
    webbrowser.open('https://github.com/goncalvesmatheus/sorteio_MegaSena')

# Function when press the button OK to send how many lists do you want.
def btnok():
    s.sorteio(repeat)
    txtArea.delete(1.0, END)
    for key, values in s.result.items():
        txtArea.insert(END, str(values)+'\n')
    s.result = {}


# **------- Main -------**
# Main window for the interface (default)
root = Tk()

# Change the title in the window
root.title('Numbers for lottery')

# Create menu bar
menu = Menu(root)
root.config(menu=menu)

# Create submenu File, cascade mode with options (submenu)
subMenuFile = Menu(menu)
menu.add_cascade(label="File", menu=subMenuFile)
subMenuFile.add_command(label="Advanced", command=s.advancedMode)
subMenuFile.add_separator()
subMenuFile.add_command(label="Exit", command=on_closing)

# Create submenu Help, cascade mode with options (submenu)
subMenuHelp = Menu(menu)
menu.add_cascade(label="Help", menu=subMenuHelp)
subMenuHelp.add_command(label="Project", command=projectURL)
subMenuHelp.add_separator()
subMenuHelp.add_command(label="About", command=aboutInf)

# Create the label and entry text field
label_qtd = Label(root, text='How many lists do you want?')
entry_qtd = Entry(root)

# Variable receiving the entry text field (in this case, string type)
repeat = entry_qtd
# Create the button, calling the function in another script, passing parameter (repeat)
btn_ok = Button(root, text='OK', command=btnok)

# Put the label, button and entry text field in grid layout inside the Main area
label_qtd.grid(row=0, column=0, sticky=E)
entry_qtd.grid(row=0, column=1)
btn_ok.grid(columnspan=2)


# Frame to return information + configs (Type Text Area)
frame = Frame(root).grid(columnspan=2)
txtArea = Text(frame, width=30, height=3)
txtArea.grid(columnspan=2)


# Calling the function when closing the window
root.protocol("WM_DELETE_WINDOW", on_closing)


# Start the interface
root.mainloop()
