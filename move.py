class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving 🚗"


class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying ✈️"


class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing 🚤"


# Example usage
if __name__ == "__main__":
    car = Car("Tesla Model S")
    plane = Plane("Boeing 747")
    boat = Boat("Yacht")

    vehicles = [car, plane, boat]

    for vehicle in vehicles:
        print(vehicle.move())