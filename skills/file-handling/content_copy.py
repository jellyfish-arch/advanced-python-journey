source = "sample.txt"
destination = "copy.txt"

with open(source, "r") as s, open(destination, "w") as d:
    d.write(s.read())

print("File copied")
