class FileManager:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        print("Opening file...")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        self.file.close()


with FileManager("test.txt", "w") as f:
    f.write("Hello Context Manager")
