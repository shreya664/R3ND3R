from tkinter import *
from tkinter import messagebox, filedialog
import os
import shutil


root = Tk()
root.geometry("885x660")
root.title("R3ND3R UI")
root.config(background="#5D6D7E")


def open_file():
    file = filedialog.askopenfilename()
    os.startfile(file)
    messagebox.showinfo('Render your Model', file+" Model rendered successfully.")


def delete_file():
    file = filedialog.askopenfilename()
    os.remove(file)
    messagebox.showinfo('Delete your Model', file+"Model deletion successful.")

    
def rename_file():
    global filename, file, f1, path
    file = filedialog.askopenfilename()
    path = os.path.abspath(file)
    f1 = Frame(root, background="grey")
    f1.grid(row=6, column=2)
    Label(f1, text="Enter the Model(File) Name").grid(row=0, column=1, padx=10, pady=10)
    filename = Entry(f1)
    filename.grid(row=1, column=1, padx=10, pady=10)
    Button(f1, text='Rename your Model', command=change_name).grid(row=2, column=1, padx=10, pady=10)
    Button(f1, text='Cancel?', command=f1.destroy).grid(row=2, column=2)
    f1.mainloop()



def change_name():
    newName = filename.get()
    dir = os.path.dirname(path)
    renamed = os.path.join(dir,newName)
    os.rename(path, renamed)
    f1.destroy()
    messagebox.showinfo('Rename your Model', file + "Model to be renamed successfully.")
