class Vehicle:
    lecenseCode = ""
    serialCode = ""
    color = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    def turnOnSportMode(self):
        print("--- Car!!! ---")
        print("Sport Mode : On")

class Van(Vehicle):
    def OpenElectronicDoors(self):
        print("--- Van!!! ---")
        print("ElectronicDoors : Open")

class PickUp(Vehicle):
    def OpenTrack(self):
        print("--- Pick Up!!! ---")
        print("Open Track")

class EstateCar(Vehicle):
    def OpenCantileverDoors(self):
        print("--- EstateCar!!! ---")
        print("Open Cantilever Doors")

car1 = Car()
car1.turnOnSportMode()
car1.turnOnAirConditioner()

van1 = Van()
van1.OpenElectronicDoors()
van1.turnOnAirConditioner()

pickup1 = PickUp()
pickup1.OpenTrack()
pickup1.turnOnAirConditioner()

EsCar = EstateCar()
EsCar.OpenCantileverDoors()
EsCar.turnOnAirConditioner()




