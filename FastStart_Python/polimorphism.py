
class Car:
    wheels = 4

    def __init__(self, name):
        self.name = name

    def driven(self):
        print(f"Driving a {self.name}")

    def start(self):
        print(f"Starting a {self.name}")

class BMW(Car):
    def start(self):
        print(f"Starting a {self.name} with a {self.wheels} wheels")

class Lada(Car):
    pass



lada = Lada('Lada')
lada.start()
lada.driven()

bmw = BMW('BMW')
bmw.start()
bmw.driven()
