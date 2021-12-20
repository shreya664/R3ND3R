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
