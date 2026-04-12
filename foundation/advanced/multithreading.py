import threading


def task(name):
    for i in range(3):
        print(f"{name} running {i}")


t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()
print("All threads completed.")
