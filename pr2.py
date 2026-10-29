class Transport:
    def __init__(self, name):
        self.name = name

    def description(self):
        return f"Транспорт - {self.name}"


class Car(Transport):
    def description(self):
        return f"Транспорт - {self.name}"


class Plane(Transport):
    def __init__(self, name, windows, wingspan):
        super().__init__(name)
        self.windows = windows
        self.wingspan = wingspan

    def description(self):
        return f"Транспорт - {self.name}, количество окон - {self.windows}, размах крыльев - {self.wingspan}"


class Bike(Transport):
    def description(self):
        return f"Транспорт - {self.name}"

bike = Bike("Харлей")
print(bike.description())

plane = Plane("Самолет", 65, "10 метров")
print(plane.description())