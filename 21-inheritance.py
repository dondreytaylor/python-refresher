class Car:
    def __init__(self, name):
        self.name = name

class Lamborghini(Car):
    pass


l = Lamborghini("Urus")
print(l.name)