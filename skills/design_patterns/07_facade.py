class CPU:
    def freeze(self):
        print("Freezing processor.")

    def jump(self, position):
        print("Jumping to:", position)

    def execute(self):
        print("Executing.")

class Memory:
    def load(self, position, data):
        print(f"Loading from {position} data: '{data}'.")

class HardDrive:
    def read(self, lba, size):
        return f"Some data from sector {lba} with size {size}"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.hard_drive.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()

if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start()
