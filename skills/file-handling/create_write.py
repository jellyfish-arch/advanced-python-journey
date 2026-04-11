filename = "sample.txt"

with open(filename, "w") as f:
    content = input("Enter text: ")
    f.write(content)

print("File written successfully")
