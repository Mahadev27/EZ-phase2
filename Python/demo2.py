class Vehicle:
    capacity=4
    wheel=4
    mileage=20
class Bike(Vehicle):
    #capacity=2
    #wheel=2
    #mileage=30
    brand='Puppy'
    def __init__(self):
        self.capacity=2
        self.wheel=2
        self.mileage=30
b=Bike()
print(b.capacity)
print(type(b))
