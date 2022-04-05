from asyncio.windows_utils import BUFSIZE
import sys
import os
import hashlib
from tkinter import filedialog

import pathlib

path = filedialog.askdirectory()
colpath = filedialog.askdirectory()

hashlist = []

for root, dirs, files in os.walk(path):
    hashind = 1
    for x in files:
        with open(str(path + "\\"+x), 'rb') as f:
            print(str("HASHING = " + str(hashind) +"/"+str(len(files))))
            hashind += 1
            digest = hashlib.sha3_224(f.read()).hexdigest()
            #print(digest)
            pair = (x,digest)
            hashlist.append(pair)
        
os.chdir(path)
i = 1
j = 1
for name1, digest1 in hashlist:
    #print(str("COMPARING =" + str(j) +"/"+str(len(hashlist))))
    j+=1
    for name2, digest2 in hashlist[i:]:
        if (digest1 == digest2 and name1 != name2):
            if pathlib.Path(name2).exists():
                print(str("COLLISION FOUND: " + name1 + " AND "+name2))
                print(str("DELETING: " + name2))
                os.remove(name2)
                with open(str(colpath.replace("/", "\\") + "\\collisions.txt"), 'a') as f:
                    print(str("COLLISION FOUND: " + name1 + " AND "+name2),file=f)
    i+=1
