filename = "sample.txt"
word = input("Enter word to search: ")

with open(filename, "r") as f:
    text = f.read()

if word in text:
    print("Word found")
else:
    print("Word not found")
