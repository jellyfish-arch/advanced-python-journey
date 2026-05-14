class EuropeanSocketInterface:
    def voltage(self):
        return 230

class USASocketInterface:
    def voltage(self):
        return 120

class Adapter(EuropeanSocketInterface):
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        return self.socket.voltage()

class ElectricKettle:
    def __init__(self, power):
        self.power = power

    def boil(self):
        if self.power.voltage() > 150:
            print("Kettle is boiling fine!")
        else:
            print("Voltage too low to boil.")

if __name__ == "__main__":
    usa_socket = USASocketInterface()
    adapter = Adapter(usa_socket)
    
    euro_socket = EuropeanSocketInterface()
    
    kettle1 = ElectricKettle(euro_socket)
    kettle1.boil()
    
    kettle2 = ElectricKettle(adapter)
    kettle2.boil()
