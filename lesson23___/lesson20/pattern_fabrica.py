l=['Car', 'Truck', 'Car', 'Bike']

class Car:
    def start(self):
        print("rrrrr")

class Truck:
    def start(self):
        print("Pshh")

class Bike:
    def start(self):
        print('Dzyn')

class Venicle:
    def __new__(cls, type):
        if type == 'Car':
            return Car()
        elif type =='Truck':
            return Truck()
        elif type == 'Bike':
            return Bike()
        else:
            raise TypeError

venicle=[Venicle(type_) for type_ in l]

for i in venicle:
    i.start()
