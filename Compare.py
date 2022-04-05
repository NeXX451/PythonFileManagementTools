from importlib.resources import path
from tkinter import filedialog
from tkinter import *
#from tkinter import simpledialog
import os
import shutil

print("TO")
path_to = filedialog.askdirectory()
print(path_to)
print("FROM")
path_from = filedialog.askdirectory()
path_copy = filedialog.askdirectory()
print(path_from)
y = input("Correct? (y)")
if str(y) == "y":
    files_to = []
    files_from = []

    for root, dirs, files in os.walk(path_to):
        files_to.extend(files)

    for root, dirs, files in os.walk(path_from):
        files_from.extend(files)

    for f in files_from:
        if not(f in files_to):
            print(f)
            shutil.copyfile(str(path_from + "\\" + f), str(path_to + "\\" + f))
            shutil.copyfile(str(path_from + "\\" + f), str(path_copy + "\\" + f))
    