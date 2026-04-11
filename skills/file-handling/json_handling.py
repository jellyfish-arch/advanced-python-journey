import json

data = {"name": "NMuis", "age": 18}

# Write JSON
with open("data.json", "w") as f:
    json.dump(data, f)

# Read JSON
with open("data.json", "r") as f:
    loaded = json.load(f)

print("Data:", loaded)
