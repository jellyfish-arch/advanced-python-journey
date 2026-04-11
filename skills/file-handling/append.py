filename = "sample.txt"

with open(filename, "a") as f:
    content = input("Enter text to append: ")
    f.write("\n" + content)

print("Content appended")
