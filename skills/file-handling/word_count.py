filename = "sample.txt"

with open(filename, "r") as f:
    text = f.read()
    words = text.split()

print("Word count:", len(words))
