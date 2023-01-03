#!/usr/bin/env python3

import os

files=[]

for file in os.listdir():
        if file == "ransomware_000.py":
                continue
        if os.path.isfile(file):
                files.append(file)

print(files)
