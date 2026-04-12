def infinite_numbers():
    n = 1
    while True:
        yield n
        n += 1


gen = infinite_numbers()

for _ in range(5):
    print(next(gen))
