class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is Flying through the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is Sailing across the water 🚢")

# Create instances of different vehicles
tesla = Car("Tesla")
boeing = Plane("Boeing 747")
yacht = Boat("Luxury Yacht")

# Demonstrate different movement methods
tesla.move()
boeing.move()
yacht.move()