import os
import shutil
from tkinter import filedialog
from tkinter import *

print("TEMP")
path_temp = filedialog.askdirectory()
print(path_temp)
print("DELETE IN")
path_deletein = filedialog.askdirectory()
print(path_deletein)

y = input("Correct? (y)")
if str(y) == "y":
    files_temp = []
    files_deletein = []
    os.chdir(path_deletein)

    for root, dirs, files in os.walk(path_temp):
        files_temp.extend(files)

    for root, dirs, files in os.walk(path_deletein):
        files_deletein.extend(files)

    for f in files_temp:
        if f in files_deletein:
            os.remove(f)