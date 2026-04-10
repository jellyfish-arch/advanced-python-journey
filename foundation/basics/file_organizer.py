import os

files = os.listdir()

for file in files:
    if file.endswith(".txt"):
        os.rename(file, "text_" + file)
