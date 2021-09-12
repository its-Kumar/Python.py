from abc import ABC, abstractmethod


class BMW(ABC):
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car ...")

    def stop(self):
        print("Stopping the car ...")

    @abstractmethod
    def drive(self):
        pass


class ThreeClass(BMW):
    def __init__(self, CuriseAssistEnabled, name, model, year):
        BMW.__init__(self, name, model, year)
        self.CuriseAssistEnabled = CuriseAssistEnabled

    def display(self):
        print(self.CuriseAssistEnabled)

    def drive(self):
        print("Three Class is being driven..")


class FiveClass(BMW):
    def __init__(self, ParkingAssistEnabled, name, model, year):
        BMW.__init__(self, name, model, year)
        self.ParkingAssistEnabled = ParkingAssistEnabled

    def display(self):
        print(self.ParkingAssistEnabled)

    def drive(self):
        print("Five Class is being driven..")


threeClass = ThreeClass(True, "BMW", "328i", 2018)
print(
    threeClass.CuriseAssistEnabled,
    threeClass.name,
    threeClass.model,
    threeClass.year
)

fiveClass = FiveClass(False, "BMW", "436j", 2017)
print(fiveClass.ParkingAssistEnabled, fiveClass.name,
      fiveClass.model, fiveClass.year)

threeClass.start()
threeClass.stop()
threeClass.drive()

fiveClass.display()
threeClass.display()
