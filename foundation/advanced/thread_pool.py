from concurrent.futures import ThreadPoolExecutor


def square(n):
    return n * n


nums = [1, 2, 3, 4, 5]

with ThreadPoolExecutor() as executor:
    results = executor.map(square, nums)

print(list(results))
