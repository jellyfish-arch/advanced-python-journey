filename = "sample.txt"

with open(filename, "r") as f:
    lines = f.readlines()

print("Total lines:", len(lines))
