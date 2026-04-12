import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f}s")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1)


slow_function()
